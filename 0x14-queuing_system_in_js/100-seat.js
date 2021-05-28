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
	if (!reservationEnabled) res.json({ status: 'Reservation are blocked' })
	const newJob = queue.create('reserve_seat', {}).save((err) => {
		if (err) res.json({ status: 'Reservation failed' })
		res.json({ status: 'Reservation in process' })
	})
	newJob
		.on('complete', () => console.log(`Seat reservation job ${newJob.id} completed`))
		.on('failed', (errorMessage) => console.log(`Seat reservation job ${newJob.id} failed: ${errorMessage}`))
})













// Requirements:
// Make sure to use promisify with Redis
// Make sure to use the await/async keyword to get the value from Redis
// Make sure the format returned by the web application is always JSON and not text
// Make sure that only the allowed amount of seats can be reserved
// Make sure that the main route is displaying the right number of seats
