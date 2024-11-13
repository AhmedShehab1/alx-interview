#!/usr/bin/node

const movieId = process.argv[2];

const printStarWarsCharactersName = async (movieId) => {
  try {
    let r = await fetch(`https://swapi-api.alx-tools.com/api/films/${movieId}/`); //eslint-disable-line
    r = await r.json();
    for (const characterLink of r.characters) {
      let data = await fetch(characterLink); // eslint-disable-line
      data = await data.json();
      console.log(data.name);
    }
  } catch (error) {
    console.log(`Error: ${error}`);
  }
};

printStarWarsCharactersName(movieId);
