#!/usr/bin/node
const firstArg = process.argv.slice(2);
console.log(firstArg[0] ? firstArg[0] : 'No argument');