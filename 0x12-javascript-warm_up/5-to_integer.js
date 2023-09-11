#!/usr/bin/node
const args = process.argv.slice(2);
num = Number(args[0]);
console.log(num ? 'My number: ' + num : 'Not a number');
