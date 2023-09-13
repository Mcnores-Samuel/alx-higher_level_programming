#!/usr/bin/node
/**
 * @list - array to search occurance of the element
 * @searchElement - item or element to search
 * @returns - returns the number of occurrences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(elem => {
    if (elem === searchElement) count++;
  });
  return count;
};
