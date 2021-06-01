import redis from 'redis'
const { promisify } = require('util')

const client = redis.createClient()

const asyncSet = promisify(client.set).bind(client)
const asyncGet = promisify(client.get).bind(client)

client.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`))
client.on('connect', () => console.log('Redis client connected to the server'))

const setNewSchool = async (schoolName, value) => console.log(`Reply: ${await asyncSet(schoolName, value)}`)
const displaySchoolValue = async (schoolName) => console.log(await asyncGet(schoolName))

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
