export default function getListStudentIds(array) {
  return Array.isArray(array) ? array.map((student) => student.id) : [];
}
