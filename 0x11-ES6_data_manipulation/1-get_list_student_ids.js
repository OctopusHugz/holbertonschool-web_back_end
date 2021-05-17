const getListStudentIds = (a) => (Array.isArray(a) ? a.map((student) => student.id) : []);
export default getListStudentIds;
