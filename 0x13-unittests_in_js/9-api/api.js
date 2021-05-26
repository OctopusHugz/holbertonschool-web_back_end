const express = require('express')

const app = express()
const port = 7865

app.listen(port, console.log(`API available on localhost port ${port}`))
app.get('/', (req, res) => res.end('Welcome to the payment system'))
app.get('/cart/:id([0-9]*)', (req, res) => res.end(`Payment methods for cart ${req.params.id}`))
