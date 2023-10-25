#!/usr/bin/node
// writes a string to a file

const filesystem = require('fs').promises;
const args = process.argv.slice(2);
const pathname = args[0];
const data = args[1];

/**
 * readFile - writes a string to a file
 * @filepath - pathname of the file to write to.
 */
async function writeFile (filepath, text) {
  try {
    await filesystem.writeFile(filepath, text);
  } catch (error) {
    console.log(error);
  }
}

writeFile(pathname, data);
