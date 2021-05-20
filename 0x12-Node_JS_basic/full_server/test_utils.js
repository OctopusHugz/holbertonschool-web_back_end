import readDatabase from './utils';

readDatabase('nope.csv')
  .then(() => {
    console.log('Done!');
  })
  .catch((error) => {
    console.log(error);
  });
