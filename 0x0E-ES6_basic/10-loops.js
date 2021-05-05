export default function appendToEachArrayValue(array, appendString) {
	for (let val of array) {
    array[array.indexOf(val)] = appendString + val;
  }

  return array;
}
