'use strict';

//BOM Browser Object Model
console.log(window);


// CONFIRM -voidaan käyttää esim if-lauseen ehtona (boolean-value)
if (confirm('Ookko tosissas?')){
  console.log(confirm('Käyttäjä painoi OK.'));
} else {
  console.log('Käyttäjä muutti mielensä!');
}


//DOM - Document Object Model
// querySelector() palauttaa yhden vs, querySelectorAll()
console.log(window.document); // voi kirjoittaa myös pelkkä (document)
const targetElement = document.getElementsByName('moi');
const tagNameEsim = document.getElementsByTagNameNS('p');
// document.getElementById(#nyt_ei _le.);
const targetElement = document.querySelector(#tähän_id, vaikka otsikko tai tekstikontentti);

//Katso opettajan esimerkki
