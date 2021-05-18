export default function createInt8TypedArray(length, position, number) {
  const buffer = new ArrayBuffer(length);
  const int8View = new Int8Array(buffer);
  if (position >= 0 && position < length) { int8View.set([number], position); } else { throw Error('Position outside range'); }
  return int8View;
  // const dataView = new DataView(buffer);
  // if (position < length) { dataView.setUint8(position, number); } else { throw Error('Position outside range'); }
  // return dataView;
}
