// Write a program that rolls user defined number of dice and displays the sum of the results of the dice rolls.(2p)
// First, program asks the user for the number of dice rolls.
// Then the program throws a die as many times as the user defined.
// Print the sum of the results in the console or in the HTML document.

'use strict';
const summa = document.querySelector('#printtaus');

const heitot = prompt('Anna noppien määrä: ');
const yhteensä = [];

for ( let i = 1; i <= heitot; i +=1 ) {
  const noppa = Math.floor(Math.random() * 6 + 1)
  yhteensä.push(noppa)
}

console.log(yhteensä);
let sum = 0;

for (let w = 0; w < yhteensä.length; w += 1) {
  sum += yhteensä[w]
}

summa.innerHTML = `Noppien silmälukujen summa on ${sum}.`;

