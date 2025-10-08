#!/usr/bin/node

const args = process.argv.slice(2).map(arg => parseInt(arg));

if (args.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const filtered = args.filter(num => num !== max);
  const secondMax = filtered.length === 0 ? 0 : Math.max(...filtered);
  console.log(secondMax);
}
