import createEmployeesObject from './11-createEmployeesObject';
import createReportObject from './12-createReportObject';
import createIteratorObject from './100-createIteratorObject';
import iterateThroughObject from './101-iterateThroughObject';

const employees = {
  ...createEmployeesObject('engineering', ['Bob', 'Jane']),
  ...createEmployeesObject('marketing', ['Sylvie', 'John']),
  ...createEmployeesObject('design', ['Dave', 'Mike']),
};

const report = createReportObject(employees);
const reportWithIterator = createIteratorObject(report);

const iterArray = [];

for (const item of reportWithIterator) {
  iterArray.push(item);
}

describe('testing task 12', () => {
  it('checks report contents', () => {
    expect.assertions(2);
    expect(report.allEmployees).toStrictEqual({ engineering: ['Bob', 'Jane'], marketing: ['Sylvie', 'John'], design: ['Dave', 'Mike'] });
    expect(report.getNumberOfDepartments(report.allEmployees)).toBe(3);
  });
});

describe('testing task 13', () => {
  it('checks report with iterator contents', () => {
    expect.assertions(6);
    expect(iterArray[0]).toBe('Bob');
    expect(iterArray[1]).toBe('Jane');
    expect(iterArray[2]).toBe('Sylvie');
    expect(iterArray[3]).toBe('John');
    expect(iterArray[4]).toBe('Dave');
    expect(iterArray[5]).toBe('Mike');
  });
});

describe('testing task 14', () => {
  it('iterates through report object with 6 names', () => {
    expect.assertions(1);
    expect(iterateThroughObject(reportWithIterator)).toBe('Bob | Jane | Sylvie | John | Dave | Mike');
  });
});
