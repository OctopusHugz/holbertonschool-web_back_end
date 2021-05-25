const { expect } = require("chai");
const sinon = require("sinon");

const sendPaymentRequestToApi = require("./3-payment");

describe('sendPaymentRequestToApi', () => {
	let consoleSpy = sinon.spy(console, 'log')

	it('validates usage of Utils.calculateNumber', () => {
		sendPaymentRequestToApi(100, 20)

		expect(consoleSpy.calledWith('The total is: 120')).to.be.true
	})

	consoleSpy.restore()
})
