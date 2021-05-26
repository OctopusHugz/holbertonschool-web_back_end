const { expect } = require("chai");
const request = require('request')

describe('Index page', () => {
	it('checks output of curling server for index page with valid cart number', (done) => {
		request('http://localhost:7865/cart/12', (error, response, body) => {
			expect(response.statusCode).to.equal(200)
			expect(body).to.equal('Payment methods for cart 12')
		}, done())
	})
	it('checks output of curling server for index page with invalid cart number', (done) => {
		request('http://localhost:7865/cart/hello', (error, response, body) => {
			if (response) {
				expect(response.statusCode).to.equal(404)
				expect(response.body).to.equal('')
			}
		}, done())
	})
})
