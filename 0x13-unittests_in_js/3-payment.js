const Utils = require('./utils')
const calculateNumber = Utils.calculateNumber

function sendPaymentRequestToApi(totalAmount, totalShipping) {
	const finalTotal = calculateNumber('SUM', totalAmount, totalShipping)
	console.log(`The total is: ${finalTotal}`)
}
