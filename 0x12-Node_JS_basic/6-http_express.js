const express = require('express');
const helpers = require('./helpers');

const { writeIndex } = helpers;

const hostname = '127.0.0.1';
const port = 1245;

const app = express();

app.get('/', (req, res) => writeIndex(res));

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
