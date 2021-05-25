function getPaymentTokenFromAPI(success) {
	if (success) {
		const p = new Promise((resolve, reject) => {
			resolve({ data: 'Successful response from the API' })
		})
		return p
	}
}

module.exports = getPaymentTokenFromAPI;
