const { expect } = require("chai");
const sinon = require("sinon");

const sendPaymentRequestToApi = require("./3-payment");

describe('sendPaymentRequestToApi', () => {
	it('validates usage of Utils.calculateNumber', () => {
		let consoleSpy = sinon.spy(console, 'log')
		sendPaymentRequestToApi(100, 20)

		expect(consoleSpy.calledWith('The total is: 120')).to.be.true
		consoleSpy.restore()
	})
})
