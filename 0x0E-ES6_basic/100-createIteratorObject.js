export default function createIteratorObject(report) {
  const employeeArray = [];
  for (const iterator of Object.keys(report.allEmployees)) {
    employeeArray.push(...report.allEmployees[iterator]);
  }
  const customIter = {
    [Symbol.iterator]() {
      let count = 0;
      return {
        next() {
          if (count < Object.keys(report.allEmployees).length + 1) {
            count += 1;
            return { done: false, value: employeeArray[count - 1] };
          }
          return { done: true, value: undefined };
        },
      };
    },
  };
  return customIter;
}
