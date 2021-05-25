const { expect } = require("chai");
const sinon = require("sinon");

const getPaymentTokenFromApi = require("./6-payment_token");

describe('getPaymentTokenFromApi', () => {
	it('checks output of getPaymentTokenFromApi with true as succcess', (done) => {
		getPaymentTokenFromApi(true)
			.then((response) => {
				expect(response).to.deep.equal({ data: 'Successful response from the API' })
			}).then(done, done)
	})
	it('checks output of getPaymentTokenFromApi with false as succcess', () => {
		expect(getPaymentTokenFromApi(false)).to.be.undefined
	})
})
