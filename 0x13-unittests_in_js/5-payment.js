const Utils = require('./utils')

function sendPaymentRequestToApi(totalAmount, totalShipping) {
	const finalTotal = Utils.calculateNumber('SUM', totalAmount, totalShipping)
	console.log(`The total is: ${finalTotal}`)
}

module.exports = sendPaymentRequestToApi;
