#!/usr/bin/node
/* eslint-disable */
// 0-starwars_characters.js
const request = require('request');

const movieId = process.argv[2]; // The movie ID passed as a positional argument

if (!movieId) {
  console.log('Please provide a movie ID');
  process.exit(1);
}

// URL to fetch movie details
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch JSON data using a URL
function fetchJson (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      if (response.statusCode !== 200) {
        return reject(`Failed to fetch data from ${url}`);
      }
      resolve(JSON.parse(body));
    });
  });
}

// Main function to fetch movie data and display character names in order
async function printCharacterNames () {
  try {
    const movieData = await fetchJson(apiUrl);
    const characterUrls = movieData.characters;

    // Fetch all character data while preserving order
    const characterPromises = characterUrls.map(url => fetchJson(url));
    const characters = await Promise.all(characterPromises);

    // Print each character's name in order
    characters.forEach(character => console.log(character.name));
  } catch (error) {
    console.error('Error:', error);
  }
}

printCharacterNames();
