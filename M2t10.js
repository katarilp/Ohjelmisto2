'use strict';

//The program asks for the number of candidates.
// Then the program asks for the names of the candidates: 'Name for candidate 1
// Store the candidates' names and initial vote count in objects like this:

const ehdokkaidenMaara = parseInt(prompt('Anna ehdokkaiden määrä: '));
const aanestajat = parseInt(prompt('Anna äänestäjien määrä: '));


const ehdokkaat = []
for (let i = 0; i < ehdokkaidenMaara; i++) {
  const ehdokkaanNimi = prompt(`Anna ehdokkaan ${i} nimi: `)
  let ehdokasolio = {nimi: `${ehdokkaanNimi}`, id: {i}, saldo: 0}
  ehdokkaat.push(ehdokasolio)
}

for (let W = 0; W < aanestajat; W++) {
  const vaalinumero = parseInt(prompt('Anna ehdokkaasi äänestysnumero: '))
  ehdokkaat[vaalinumero].saldo += 1;
}

ehdokkaat.
console.log(ehdokkaat);
