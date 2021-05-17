export default function createInt8TypedArray(length, position, number) {
  const buffer = new ArrayBuffer(length);
  const dataView = new DataView(buffer);
  if (position < length) { dataView.setUint8(position, number); } else { throw Error('Position outside range'); }
  return dataView;
}
