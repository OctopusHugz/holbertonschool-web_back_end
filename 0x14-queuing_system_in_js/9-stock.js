import express from 'express'

const listProducts = [
	{ id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
	{ id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
	{ id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
	{ id: 4, name: 'Suitcase 1050', price: 50, stock: 5 }
]

// The .filter() below will fail accessing [0] if no product in listProducts has that id
const getItemById = (id) => listProducts.filter((product) => product.id === id)[0]

const app = express()
const PORT = 1245
app.listen(PORT, console.log(`Server listening on localhost:${PORT}`))

// Make sure to use promisify with Redis
// Make sure to use the await/async keyword to get the value from Redis
// Make sure the format returned by the web application is always JSON and not text
