#!/usr/bin/node
const args = process.argv.slice(2);
const num = Number(args[0]);
if (!num) {
  console.log('Missing size');
} else {
  for (let n = 0; n < num; n++) console.log('X'.repeat(num));
}
