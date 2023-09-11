#!/usr/bin/node
const cmdLineArgs = process.argv.slice(2);
const numOfArgs = cmdLineArgs.length;
if (numOfArgs === 0) {
  console.log('No argument');
} else if (numOfArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
};
