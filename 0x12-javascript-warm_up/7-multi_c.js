#!/usr/bin/node
const args = process.argv.slice(2);
const num = Number(args[0]);
if (!num) {
  console.log('Missing number of occurrences');
} else {
  for (let n = 0; n < num; n++) console.log('C is fun');
}
