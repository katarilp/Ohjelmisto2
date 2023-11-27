// Write a program that asks the user for the number of participants.
// After this, the program asks for the names of all participants.
// Finally, the program prints the names of the participants on the web page
// in an ordered list (<ol>) in alphabetical order.

'use strict';
const luku = parseInt(prompt('Anna osallistujien määrä: '));
const osallistujat = [];

for (let i = 0; i < luku; i ++) {
  const uusiNimi = prompt('Osallistujan nimi: ');
  osallistujat.push(uusiNimi);
}

osallistujat.sort();
console.log(osallistujat);


for (let i = 0; i < luku; i++) {
  document.querySelector('#kohde').innerHTML = (`${osallistujat[i]}`)
  }







