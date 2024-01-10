#!/usr/bin/node

function factorial (num) {
  if (num === 1 || num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

if (isNaN(Number(process.argv[2]))) {
  console.log(1);
} else {
  const result = factorial(Number(process.argv[2]));
  console.log(result);
}
