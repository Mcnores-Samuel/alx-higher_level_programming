#!/usr/bin/node
/**
 * @list - an array to reverse
 * @returns -  returns the reversed version of a list
 */
exports.esrever = function (list) {
  const copyArr = [];
  for (let offset = list.length - 1; offset >= 0; offset--) copyArr.push(list[offset]);
  return copyArr;
};
