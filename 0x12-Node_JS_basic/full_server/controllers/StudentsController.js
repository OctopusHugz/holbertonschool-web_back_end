import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    response.statusCode = 200;
    // await readDatabase();
  }

  static getAllStudentsByMajor(request, response) {
    response.statusCode = 200;
    const { major } = request.params;
    // await readDatabase();
  }
}

export default StudentsController;
