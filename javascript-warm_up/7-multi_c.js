#!/usr/bin/node

const arg = process.argv[2];
const count = parseInt(arg);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  let output = '';
  while (i < count) {
    output += 'C is fun\n';
    i++;
  }
  console.log(output.trim());
#!/usr/bin/node

const arg = process.argv[2];
const count = parseInt(arg);

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else if (count > 0) {
  let i = 0;
  let output = '';
  while (i < count) {
    output += 'C is fun\n';
    i++;
  }
  console.log(output.trim());
}}
