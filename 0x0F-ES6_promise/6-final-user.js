import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then(
      (results) => {
        const newArray = [];
        for (let i = 0; i < results.length; i += 1) {
          if (results[i].status === 'fulfilled') { newArray.push({ status: results[i].status, value: results[i].value }); } else { newArray.push({ status: results[i].status, value: `Error: ${results[i].reason.message}` }); }
        }
        return newArray;
      },
    );
}
