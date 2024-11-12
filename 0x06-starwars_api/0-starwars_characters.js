#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2];
const mainURL = 'https://swapi-api.alx-tools.com/api/films/';

new Promise((resolve, reject) => {
  request(mainURL + filmNum, function (error, response, body) {
    if (error) {
      reject(error);
      return;
    }
    try {
      resolve(JSON.parse(body).characters);
    } catch (error) {
      reject(error);
    }
  });
}).then(
  (URLs) => {
    const names = [];

    for (const url of URLs) {
      names.push(new Promise((resolve, reject) => {
        request(url, (err, resp, body) => {
          if (err) {
            reject(err);
            return;
          }
          try {
            resolve(JSON.parse(body).name);
          } catch (err) {
            reject(err);
          }
        });
      }));
    }
    Promise.all(names).then((res) => {
      res.forEach((name) => console.log(name));
    }); // returns the result in order regardless of the time
  },
  (Err) => console.log(Err)
);
