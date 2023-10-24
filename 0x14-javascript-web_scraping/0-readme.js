#!/usr/bin/node
// reads and prints the content of a file.

const filesystem = require('fs').promises;
const pathname = process.argv.slice(2)[0];

/**
 * readFile - reads and prints the content of a file.
 * @filepath - pathname of the file to read.
 */
async function readFile (filepath) {
  try {
    const data = await filesystem.readFile(filepath);
    console.log(data.toString());
  } catch (error) {
    console.log(error);
  }
}

readFile(pathname);
