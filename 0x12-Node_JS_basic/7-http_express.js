const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  await countStudents(process.argv[2]).then((value) => {
    res.write('This is the list of our students\n');
    res.write(`Number of students: ${value.students.length}\n`);
    res.write(`Number of students in CS: ${value.csStudents.length}. List: ${value.csStudents.join(', ')}\n`);
    res.write(`Number of students in SWE: ${value.sweStudents.length}. List: ${value.sweStudents.join(', ')}`);
    res.end();
  }).catch((err) => res.send(err.message));
});

app.listen(1245);

module.exports = app;
