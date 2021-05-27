import redis from 'redis'
const { promisify } = require('util')

const runApp = async () => {
	const client = redis.createClient()

	client.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`))
	client.on('connect', () => console.log('Redis client connected to the server'))

	const setNewSchool = (schoolName, value) => client.set(schoolName, value, redis.print)
	const displaySchoolValue = async (schoolName) => {
		const promisifiedFunc = promisify(client.get).bind(client)
		console.log(await promisifiedFunc(schoolName))
	}

	await displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');
}

runApp()
