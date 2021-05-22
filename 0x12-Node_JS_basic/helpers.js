function writeResponse(res, data, showTotal) {
  res.statusCode = 200;
  res.write('This is the list of our students\n');

  if (showTotal) res.write(`Number of students: ${data.students.length}\n`);
  res.write(`Number of students in CS: ${data.csStudents.length}. List: ${data.csStudents.join(', ')}\n`);
  res.end(`Number of students in SWE: ${data.sweStudents.length}. List: ${data.sweStudents.join(', ')}`);
}

module.exports = writeResponse;
