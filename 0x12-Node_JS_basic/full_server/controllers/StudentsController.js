import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((value) => {
        response.statusCode = 200;
        response.write('This is the list of our students\n');
        response.write(`Number of students in CS: ${value.csStudents.length}. List: ${value.csStudents.join(', ')}\n`);
        response.end(`Number of students in SWE: ${value.sweStudents.length}. List: ${value.sweStudents.join(', ')}`);
      })
      .catch((err) => {
        // response.status(500).send('Cannot load the database');
        response.statusCode = 500;
        response.statusMessage = err.message;
        response.end(`${err.message}`);
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (['CS', 'SWE'].indexOf(major) === -1) { response.status(500).send('Major parameter must be CS or SWE'); }

    readDatabase(process.argv[2])
      .then((value) => {
        response.statusCode = 200;
        if (major === 'CS') { response.end(`List: ${value.csStudents.join(', ')}`); } else {
          response.end(`List: ${value.sweStudents.join(', ')}`);
        }
      })
      .catch((err) => {
        // response.status(500).send('Major parameter must be CS or SWE');
        response.statusCode = 500;
        response.statusMessage = err.message;
        response.end(`${err.message}`);
      });
  }
}

export default StudentsController;
