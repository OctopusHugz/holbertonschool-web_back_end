export default function getStudentIdsSum(studentList) {
  return studentList.reduce((total, val) => total + val.id, 0);
}
