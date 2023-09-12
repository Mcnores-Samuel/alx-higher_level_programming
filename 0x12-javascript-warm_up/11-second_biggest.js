#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const arrOfNums = args.map((elem) => Number(elem)).sort((a, b) => a - b);
  const secondMax = arrOfNums[arrOfNums.length - 2];
  console.log(secondMax);
}
