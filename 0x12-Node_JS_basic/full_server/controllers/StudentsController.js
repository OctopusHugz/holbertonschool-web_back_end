import readDatabase from '../utils';
import { writeResponse, writeMajorList } from '../../helpers';

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((data) => writeResponse(response, data, false))
      .catch((err) => response.status(500).send(err.message));
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;
    if (['CS', 'SWE'].indexOf(major) === -1) { response.status(500).send('Major parameter must be CS or SWE'); }

    readDatabase(process.argv[2])
      .then((data) => writeMajorList(response, data, major))
      .catch((err) => response.status(500).send(err.message));
  }
}

export default StudentsController;
