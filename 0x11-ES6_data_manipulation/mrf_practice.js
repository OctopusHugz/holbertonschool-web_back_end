const data = [
  {
    mood: 'happy',
    fish: 'robin',
    colours: ['blue', 'green'],
  },
  {
    mood: 'tired',
    fish: 'panther',
    colours: ['green', 'black', 'orange', 'blue'],
  },
  {
    mood: 'sad',
    fish: 'goldfish',
    colours: ['green', 'red'],
  },
];

const collection = [
  {
    name: 'apple',
    weight: 0.18,
    id: 0,
  },
  {
    name: 'banana',
    weight: 0.25,
    id: 1,
  },
  {
    name: 'avocado',
    weight: 0.31,
    id: 2,
  },
  {
    name: 'watermelon',
    weight: 1.85,
    id: 3,
  },
];

const collectionTwo = [
  {
    name: 'apple',
    bestBefore: '2021-06-10',
  },
  {
    name: 'banana',
    bestBefore: '2017-01-05',
  },
  {
    name: 'pear',
    bestBefore: '2016-12-10',
  },
  {
    name: 'cantaloupe',
    bestBefore: '2021-10-05',
  },
  {
    name: 'khaki',
    bestBefore: '2016-12-24',
  },
];

const fruitNames = collection.map((item) => item.name);
const fruitObjs = collection.map((item) => {
  const newItem = {};
  newItem[item.name] = item.weight;
  return newItem;
});
const freshFruit = collectionTwo.filter((fruit) => {
  const bestBefore = new Date(fruit.bestBefore);
  const now = new Date();

  return bestBefore > now;
});

console.log(fruitNames);
console.log(fruitObjs);
console.log(freshFruit);

const coloursArray = data.map((e) => e.colours);

const flatArray = coloursArray.reduce((total, subArray) => total.concat(subArray));

const uniqueArray = flatArray.filter((element, index, array) => array.indexOf(element) === index);

function getColorsFromArray(array) {
  return array.map((e) => typeof e.colours !== 'undefined' && e.colours);
}

function flattenArray(array) {
  return array.reduce((total, next) => total.concat(next));
}

function getUniqueItems(array) {
  return array.filter((e, i, self) => self.indexOf(e) === i);
}

function sortItems(array) {
  return array.sort();
}

const pipeline = [getColorsFromArray, flattenArray, getUniqueItems, sortItems];
const result = pipeline.reduce((total, func) => func(total), data);

console.log(uniqueArray);
console.log(result);
console.log(result.includes('green'));

const movie = new Map();
movie.set('name', 'Killers of the Flower Moon');
movie.set('releaseYear', 2021);
console.log(movie.get('name'));
console.log(movie.get('releaseYear'));
console.log(movie.has('name') && movie.has('releaseYear'));

for (const attr of movie) {
  console.log(attr);
}

function replacer(key, value) {
  if (value instanceof Map) {
    return {
      dataType: 'Map',
      value: Array.from([...value]),
    };
  }
  return value;
}

function reviver(key, value) {
  if (typeof value === 'object' && value !== null) {
    if (value.dataType === 'Map') {
      return new Map(value.value);
    }
  }
  return value;
}

const str = JSON.stringify(movie, replacer);
const newValue = JSON.parse(str, reviver);
console.log(Object.entries(movie).toString() === Object.entries(newValue).toString());
console.log(newValue.size);
console.log(typeof movie[Symbol.iterator] === 'function');
