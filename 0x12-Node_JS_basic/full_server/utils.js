// import readFile } from 'fs/promises';
import fs from 'fs';

export default async function readDatabase(path) {
  // if (!fs.existsSync(path)) {
  //   throw Error('Cannot load the database');
  // }

	const data = await fs.readFile(path);
	return new Promise((resolve, reject) => {
		
	})

  // const data = await fs.readFile(path)
  //   .then((value) => console.log(value), () => { throw new Error('Cannot load the database'); })
  //   .catch((err) => console.log(err.message));
  // return data;
}

// It should read the database asynchronously
// It should return a promise

// When the file is not accessible,
// it should reject the promise with the error

// When the file can be read,
// it should return an object of arrays of the firstname of students per fields
