export default function divideFunction(numerator, denominator) {
  let quotient = 0;
  if (denominator === 0) {
    throw Error('cannot divide by 0');
  }
  try {
    quotient = numerator / denominator;
  } catch (error) {
    console.log(error);
  }
  return quotient;
}
