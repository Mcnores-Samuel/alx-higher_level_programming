#!/usr/bin/node
const numOfArgs = process.argv.slice(2).length;
if (numOfArgs === 0) console.log('No argument');
if (numOfArgs === 1) console.log('Argument found');
if (numOfArgs > 1) console.log('Arguments found');
