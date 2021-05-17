export default function updateStudentGradeByCity(studentList, city, newGrades) {
  return studentList
    .filter((student) => student.location === city)
    .map((student) => {
      let newGrade = 'N/A';
      newGrades.forEach((gradeObj) => {
        if (gradeObj.studentId === student.id) newGrade = gradeObj.grade;
      });
      return { ...student, grade: newGrade };
    });
}
