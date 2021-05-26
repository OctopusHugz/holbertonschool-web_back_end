const express = require('express')

const app = express()
const port = 7865

app.listen(port, console.log(`API available on localhost port ${port}`))
app.get('/', (req, res) => res.end('Welcome to the payment system'))
app.get('/cart/:id', (req, res) => {
	const idArray = req.params.id.match(/(\d+)/);
	if (idArray) res.end(`Payment methods for cart ${idArray[0]}`)
	else res.status(404).end()
})
