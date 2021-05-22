const express = require('express');
const countStudents = require('./3-read_file_async');
const writeResponse = require('./helpers');

const app = express();

app.get('/', (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  countStudents(process.argv[2])
    .then((data) => writeResponse(res, data, true))
    .catch((err) => res.status(404).send(`This is the list of our students\n${err.message}`));
});

app.listen(1245);

module.exports = app;
