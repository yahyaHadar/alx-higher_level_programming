#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: node 5-request_store.js <url> <file_path>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else {
    fs.writeFile(filePath, body, 'utf-8', (writeError) => {
      if (writeError) {
        console.error(`Error writing to file: ${writeError.message}`);
      }
    });
  }
});
