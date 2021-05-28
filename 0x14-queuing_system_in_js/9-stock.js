const express = require('express')
const redis = require('redis')
const { promisify } = require('util')

const app = express()
const client = redis.createClient()

const promisifiedSet = promisify(client.set).bind(client)
const asyncGet = promisify(client.get).bind(client)

const listProducts = [
	{ itemId: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
	{ itemId: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
	{ itemId: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
	{ itemId: 4, name: 'Suitcase 1050', price: 50, initialAvailableQuantity: 5 }
]
const port = 1245

// The .filter() below will fail accessing [0] if no product in listProducts has that id
const getItemById = (id) => listProducts.filter((product) => product.itemId === id)[0]

app.listen(port, console.log(`Stock app listening at http://localhost:${port}`))
app.get('/list_products', (req, res) => res.json(listProducts))
app.get('/list_products/:itemId', async (req, res) => {
	const itemId = req.params.itemId
	const rObj = getItemById(parseInt(itemId))
	if (!rObj) res.json({ status: 'Product not found' })
	const currentStock = await getCurrentReservedStockById(itemId)
	if (!currentStock) {
		await reserveStockById(itemId, rObj.initialAvailableQuantity)
		rObj.currentQuantity = rObj.initialAvailableQuantity
	}
	else {
		await reserveStockById(itemId, currentStock - 1)
		rObj.currentQuantity = currentStock - 1
	}
	res.json(rObj)
})

client.on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`))
client.on('connect', () => console.log('Redis client connected to the server'))

const reserveStockById = (itemId, stock) => promisifiedSet(`item.${itemId}`, stock)
const getCurrentReservedStockById = async (itemId) => await asyncGet(`item.${itemId}`)
