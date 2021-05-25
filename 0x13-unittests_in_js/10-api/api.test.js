const { expect } = require("chai");
const request = require('request')

describe('Login page', () => {
	it('checks output of curling login page with userName data', (done) => {
		const options = {
			url: 'http://localhost:7865/login',
			method: 'POST',
			json: { 'userName': 'Betty' }
		}
		request(options, (error, response, body) => {
			expect(response.statusCode).to.equal(200)
			expect(response.body).to.equal('Welcome: Betty')
		}, done())
	})
})


describe('Available payments page', () => {
	it('checks output of curling available_payments page', (done) => {
		request('http://localhost:7865/available_payments', (error, response, body) => {
			expect(response.statusCode).to.equal(200)
			expect(response.body).to.deep.equal(JSON.stringify({
				payment_methods: {
					credit_cards: true,
					paypal: false
				}
			}))
		}, done())
	})
})
