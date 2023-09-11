#!/usr/bin/node
/**
 * add - prints the addition of 2 integers
 * @a - first integer
 * @b - second inter
 */
function add (a, b) {
  console.log(a + b);
}

const args = process.argv.slice(2);
const a = Number(args[0]);
const b = Number(args[1]);
add(a, b);
