#!/usr/bin/node
/**
 * factorial - computes and prints a factorial
 * @num - integer to factorize
 * @returns a factorial of a number
 */
const factorial = (num) => {
  if (!num || num === 1) {
    return (1);
  } else {
    return factorial(num - 1) * num;
  }
};

const args = process.argv.slice(2);
const num = Number(args[0]);
console.log(factorial(num));
