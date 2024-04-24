#!/usr/bin/node

const n = process.argv.length;
if (n === 2 || n === 3) {
  console.log('0');
} else {
  let arg = process.argv.slice(2);
  arg = arg.sort((a, b) => b - a);
  console.log(arg[1]);
}
