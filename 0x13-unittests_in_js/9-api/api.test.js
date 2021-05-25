const { expect } = require("chai");
const request = require('request')

describe('Index page', () => {
	it('checks output of curling server for index page', () => {
		// spy on console for API available message?
		request('http://localhost:7865', (err, res, body) => {
			expect(res.statusCode).to.equal(200)
			expect(res.body).to.equal('Welcome to the payment system')
			expect(res.request.uri.port).to.equal('7865')
		})
	})
})
