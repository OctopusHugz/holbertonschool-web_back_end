function calculateNumber(type, a, b) {
	if (['SUM', 'SUBTRACT', 'DIVIDE'].indexOf(type) !== -1) {
		if (type === 'SUM') return Math.round(a) + Math.round(b)
		else if (type === 'SUBTRACT') return Math.round(a) - Math.round(b)
		if (Math.round(b) === 0) return 'Error'
		return Math.round(a) / Math.round(b)
	} else throw new TypeError('Type must be SUM, SUBTRACT, or DIVIDE')
}

module.exports = calculateNumber
