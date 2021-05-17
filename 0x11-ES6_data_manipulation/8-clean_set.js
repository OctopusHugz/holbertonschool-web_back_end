export default function cleanSet(set, startString) {
  if (startString === '') return '';
  const setArray = Array.from(set)
    .map((item) => (item.startsWith(startString) ? item.slice(startString.length) : ''))
    .filter((item) => item !== '');
  return setArray.join('-');
}
