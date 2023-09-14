#!/usr/bin/node
const dict = require('./101-data').dict;

const array = Object.entries(dict);
const newdict = {};

for (let n = 0; n < array.length; n++) {
  const key = String(array[n][1]);
  const val = array[n][0];
  if (newdict.hasOwnProperty(key)) {
    const arr = newdict[key];
    arr.push(val);
  } else {
    newdict[key] = [val];
  }
}
console.log(newdict);
