#!/usr/bin/node

const request = require('request-promise-native');

const filmNum = process.argv[2];
const mainURL = 'https://swapi-api.alx-tools.com/api/films/';

async function printCharacters () {
  try {
    const film = await request(`${mainURL}${filmNum}`);
    const filmCharacters = JSON.parse(film).characters;

    for (const characterURL of filmCharacters) {
      try {
        const characterData = await request(characterURL);
        console.log(JSON.parse(characterData).name);
      } catch (error) {
        console.error('Error fetching character:', error.message);
      }
    }
  } catch (error) {
    console.error('Error fetching film:', error.message);
  }
}

printCharacters();
