export default function createInt8TypedArray(length, position, number) {
  const buffer = new ArrayBuffer(length);
  const int8View = new Int8Array(buffer);
  if (position < length) { int8View[position] = number; } else { throw Error('Position outside range'); }
  return buffer;
}
