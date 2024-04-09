#!/usr/bin/node
if (process.arg.length === 2) {
  console.log('No argument');
} else if (process.arg.length === 3) { console.log('Argument found'); } else {
  console.log('Arguments found');
}
