import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  // return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)]).then((results) => (results));

  // let count = 0;
  // const newArray = [];
  // const array = Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)]);
  // array.then((results) => results.forEach((result) => {
  //   if (result.status === 'fulfilled') { newArray.push({ status: result.status, value: result.value }); } else { newArray.push({ status: result.status, value: `Error: ${result.reason.message}` }); }
  //   count += 1;
  //   if (count === results.length) { return newArray; }
  // }));
  let count = 0;
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then(
      (results) => {
        const newArray = [];
        for (let i = 0; i < results.length; i += 1) {
          if (results[i].status === 'fulfilled') { newArray.push({ status: results[i].status, value: results[i].value }); } else { newArray.push({ status: results[i].status, value: `Error: ${results[i].reason.message}` }); }
        }
        return newArray;
      },
    // (results) => results.forEach((result) => {
    //   if (result.status === 'fulfilled') { newArray.push({ status: result.status, value: result.value }); } else { newArray.push({ status: result.status, value: `Error: ${result.reason.message}` }); }
    //   count += 1;
    // }),
    );
}
