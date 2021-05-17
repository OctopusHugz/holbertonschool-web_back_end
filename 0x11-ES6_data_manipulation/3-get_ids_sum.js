const getStudentIdsSum = (studentList) => studentList.reduce((total, val) => total + val.id, 0);
export default getStudentIdsSum;
