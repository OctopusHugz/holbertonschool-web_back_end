const express = require('express')
const redis = require('redis')
const kue = require('kue')
const { promisify } = require('util')

const app = express()
const client = redis.createClient()
const queue = kue.createQueue()

const promisifiedSet = promisify(client.set).bind(client)
const asyncGet = promisify(client.get).bind(client)

const reserveSeat = (number) => promisifiedSet('available_seats', number)
const getCurrentAvailableSeats = async () => asyncGet('available_seats')

const port = 1245
let reservationEnabled = true

client.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`))
client.on('connect', () => {
	console.log('Redis client connected to the server')
	reserveSeat(50)
})

app.listen(port, console.log(`Stock app listening at http://localhost:${port}`))
app.get('/available_seats', async (req, res) => {
	const seats = await getCurrentAvailableSeats()
	res.json({ numberOfAvailableSeats: seats })
})
app.get('/reserve_seat', (req, res) => {
	if (!reservationEnabled) {
		res.json({ status: 'Reservation are blocked' })
		return
	}
	const newJob = queue.create('reserve_seat', {}).save((err) => {
		if (err) res.json({ status: 'Reservation failed' })
		res.json({ status: 'Reservation in process' })
	})
	newJob
		.on('complete', () => console.log(`Seat reservation job ${newJob.id} completed`))
		.on('failed', (errorMessage) => console.log(`Seat reservation job ${newJob.id} failed: ${errorMessage}`))
})
app.get('/process', (req, res) => {
	queue.process('reserve_seat', async (job, done) => {
		const seatCount = await getCurrentAvailableSeats()
		if (seatCount > 0) reserveSeat(seatCount - 1)
		if ((seatCount - 1) === 0) reservationEnabled = false
		if ((seatCount - 1) >= 0) done()
		else return done(new Error('Not enough seats available'))
	})
	res.json({ status: 'Queue processing' })
})
