import redis from 'redis'

const client = redis.createClient()

client.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`))
client.on('connect', () => console.log('Redis client connected to the server'))

const setNewSchool = (schoolName, value) => client.set(schoolName, value, redis.print)
const displaySchoolValue = (schoolName) => client.get(schoolName, (err, reply) => console.log(reply))

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
