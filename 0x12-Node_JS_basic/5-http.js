const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  const { url } = req;
  if (url === '/') { res.send('Hello Holberton School!'); }
  if (url === '/students') {
    await countStudents(process.argv[2]).then((value) => {
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${value.students.length}\n`);
      res.write(`Number of students in CS: ${value.csStudents.length}. List: ${value.csStudents.join(', ')}\n`);
      res.write(`Number of students in SWE: ${value.sweStudents.length}. List: ${value.sweStudents.join(', ')}`);
      res.send();
    }).catch((err) => res.send(err.message));
  }
});

app.listen(1245);
module.exports = app;
