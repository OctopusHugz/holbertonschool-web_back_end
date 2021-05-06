export default function iterateThroughObject(reportWithIterator) {
  let returnString = '';
  let count = 0;
  for (const item of reportWithIterator) {
    if (count === 0) {
      returnString += item;
    } else {
      returnString += ` | ${item}`;
    }
    count += 1;
  }
  return returnString;
}
