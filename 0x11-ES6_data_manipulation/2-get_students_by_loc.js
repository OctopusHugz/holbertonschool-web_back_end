const getStudentsByLocation = (sList, city) => sList.filter((student) => student.location === city);
export default getStudentsByLocation;
