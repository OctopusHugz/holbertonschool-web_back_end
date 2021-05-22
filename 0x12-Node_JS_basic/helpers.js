function writeIndex(res) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
}

function writeResponse(res, data, showTotal) {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.write('This is the list of our students\n');

  if (showTotal) res.write(`Number of students: ${data.students.length}\n`);
  res.write(`Number of students in CS: ${data.csStudents.length}. List: ${data.csStudents.join(', ')}\n`);
  res.end(`Number of students in SWE: ${data.sweStudents.length}. List: ${data.sweStudents.join(', ')}`);
}

function writeError(res, err) {
  res.statusCode = 404;
  res.statusMessage = err.message;
  res.setHeader('Content-Type', 'text/plain');
  res.end(`This is the list of our students\n${err.message}`);
}

module.exports = writeIndex;
module.exports = writeResponse;
module.exports = writeError;
