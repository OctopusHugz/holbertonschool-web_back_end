const http = require('http');
const countStudents = require('./3-read_file_async');
const helpers = require('./helpers');

const { writeResponse } = helpers;
const { writeError } = helpers;
const { writeIndex } = helpers;

const hostname = '127.0.0.1';
const port = 1245;
const databaseFile = process.argv[2];

const app = http.createServer((req, res) => {
  const { url } = req;
  if (url === '/') writeIndex(res);
  if (url === '/students') {
    countStudents(databaseFile)
      .then((data) => writeResponse(res, data, true))
      .catch((err) => writeError(res, err));
  }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
