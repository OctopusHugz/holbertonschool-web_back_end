export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') return '';
  const setArray = [...set]
    .map((item) => (item.startsWith(startString) ? item.slice(startString.length) : ''))
    .filter((item) => item !== '');
  return setArray.join('-');
}
