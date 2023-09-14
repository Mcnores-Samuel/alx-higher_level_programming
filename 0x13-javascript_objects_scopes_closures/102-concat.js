#!/usr/bin/node
const rw = require('fs');
const args = process.argv.slice(2);

const file1 = rw.readFileSync(args[0], 'utf-8');
const file2 = rw.readFileSync(args[1], 'utf-8');
rw.writeFileSync(args[2], file1 + file2);
