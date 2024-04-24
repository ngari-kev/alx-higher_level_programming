#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

if (!isNaN(number)) {
  for (let j = 0; j < number; j++) {
    let row = '';
    for (let i = 0; i < number; i++) {
      row += 'X';
    }
	console.log(row);
  }
} else {
  console.log('Missing size');
}
