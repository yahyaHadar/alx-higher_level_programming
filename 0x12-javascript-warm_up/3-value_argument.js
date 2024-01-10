#!/usr/bin/node

const vars = process.argv;
if (vars[2]) {
  console.log(vars[2]);
} else {
  console.log('No argument');
}
