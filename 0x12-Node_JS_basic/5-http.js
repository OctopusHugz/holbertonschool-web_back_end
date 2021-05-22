const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  const { url } = req;
  let fileName;
  if (url === '/') { res.end('Hello Holberton School!'); }
  if (url === '/students') {
    try {
      [fileName] = [process.argv[2]];
    } catch (error) {
      res.statusCode = 404;
      res.end(`Error: ${error.message}`);
    }
    await countStudents(fileName).then((value) => {
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${value.students.length}\n`);
      res.write(`Number of students in CS: ${value.csStudents.length}. List: ${value.csStudents.join(', ')}\n`);
      res.end(`Number of students in SWE: ${value.sweStudents.length}. List: ${value.sweStudents.join(', ')}`);
    }).catch((err) => {
      res.statusCode = 404;
      res.end(`Error: ${err.message}`);
    });
  }
});

app.listen(1245);
module.exports = app;
