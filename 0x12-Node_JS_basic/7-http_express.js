const express = require('express');
const countStudents = require('./3-read_file_async');
const helpers = require('./helpers');

const { writeResponse, writeError, writeIndex } = helpers;

const hostname = '127.0.0.1';
const port = 1245;
const fileName = process.argv[2];

const app = express();

app.get('/', (req, res) => writeIndex(res));

app.get('/students', (req, res) => {
  countStudents(fileName)
    .then((data) => writeResponse(res, data, true))
    .catch((err) => writeError(res, err));
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
