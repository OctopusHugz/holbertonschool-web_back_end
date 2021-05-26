const { expect } = require("chai");
const request = require('request')

describe('Index page', () => {
	describe('GET /', () => {
		it('checks output of GET /', (done) => {
			request('http://localhost:7865/', (error, response, body) => {
				expect(response.statusCode).to.equal(200)
				expect(body).to.equal('Welcome to the payment system')
			}, done())
		})
	})

	describe('GET /cart/:id', () => {
		it('checks output of curling server for index page with valid cart number', (done) => {
			request('http://localhost:7865/cart/12', (error, response, body) => {
				expect(response.statusCode).to.equal(200)
				expect(body).to.equal('Payment methods for cart 12')
			}, done())
		})
	})

	describe('GET /cart/:id with id = hello', () => {
		it('checks output of curling server for index page with invalid cart number', (done) => {
			request('http://localhost:7865/cart/hello', (error, response, body) => {
				if (response) {
					expect(response.statusCode).to.equal(404)
					expect(body).to.equal('')
				}
			}, done())
		})
	})
})






