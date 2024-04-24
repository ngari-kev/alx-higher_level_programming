#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

function fact (number) {
  if (number === 0 || isNaN(number)) {
    return 1;
  } else {
    return number * fact(number - 1);
  }
}

console.log(fact(number));
