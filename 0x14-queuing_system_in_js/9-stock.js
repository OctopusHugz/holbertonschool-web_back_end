import express from 'express'

const listProducts = [
	{ itemId: 1, name: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
	{ itemId: 2, name: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
	{ itemId: 3, name: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
	{ itemId: 4, name: 'Suitcase 1050', price: 50, initialAvailableQuantity: 5 }
]

// The .filter() below will fail accessing [0] if no product in listProducts has that id
const getItemById = (id) => listProducts.filter((product) => product.id === id)[0]

const app = express()
const port = 1245

app.listen(port, console.log(`Stock app listening at http://localhost:${port}`))
app.get('/list_products', (req, res) => res.json(listProducts))

// Make sure to use promisify with Redis
// Make sure to use the await/async keyword to get the value from Redis
// Make sure the format returned by the web application is always JSON and not text
