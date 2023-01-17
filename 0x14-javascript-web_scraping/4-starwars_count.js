#!/usr/bin/node
const request = require('request');
const endpoint = process.argv[2];
let c = 0;

request(endpoint, (err, res, body) => {
  if (err) throw err;

  JSON.parse(body).results.forEach(result => {
    result.characters.forEach(character => {
      if (character.endsWith('18/')) c++;
    });
  });
  console.log(c);
});
