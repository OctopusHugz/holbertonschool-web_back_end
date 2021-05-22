const http = require('http');
const countStudents = require('./3-read_file_async');

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  const { url } = req;
  const fileName = process.argv[2];
  if (url === '/') { res.end('Hello Holberton School!'); }
  if (url === '/students') {
    countStudents(fileName).then((value) => {
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${value.students.length}\n`);
      res.write(`Number of students in CS: ${value.csStudents.length}. List: ${value.csStudents.join(', ')}\n`);
      res.end(`Number of students in SWE: ${value.sweStudents.length}. List: ${value.sweStudents.join(', ')}`);
    }).catch((err) => {
      res.statusCode = 404;
      res.statusMessage = err.message;
      res.write('This is the list of our students\n');
      res.end(`Error: ${err.message}`);
    });
  }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
module.exports = app;
