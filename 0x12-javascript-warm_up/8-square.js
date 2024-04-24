#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

if (!isNaN(number)) {
  if (number > 0) {
	for (let j = 0; j < number; j++) {
	  let row = '';
	  for (let i = 0; i < number; i++) {
		  row += 'x';
	  }
	  console.log(row);
	}
  } else {
	  console.log('Size must be greater than 0');
  }
} else {
  console.log('Missing size');
}
