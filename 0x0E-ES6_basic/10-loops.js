export default function appendToEachArrayValue(array, appendString) {
	for (let idx of array) {
    array[array.indexOf(idx)] = appendString + idx;
  }

  return array;
}
