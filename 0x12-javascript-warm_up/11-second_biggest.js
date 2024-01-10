#!/usr/bin/node

const args = process.argv.map(str => Number(str));
args.splice(0, 2);
if (args.length <= 1) {
  console.log(0);
} else {
  const sortedNums = args.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
