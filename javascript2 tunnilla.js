// Matti 15.11.2023
'use strict';

// ARRAY, alkioiden arvot voivat olla mitä vaan, (myös viittauksia muuttujiin)
//  mutta usein pyritään siihen, että taulukossa on vain yhtä tietotyyppiä,
// jotta sen käsittely olisi helpompaa. Alkiohin viitataan niiden indeksillä;
// alkaa aina nollasta, kuten listoissakin.
const items = ['eka', 2, 3.3, [1,2,3,], true];
// const sitoo yhteyden tiettyyn taulukkoon, vaikka sen sisältöä voikin muuttaa
// let käytettäisiin, jos tiedetään, että koko sisältö halutaan korvata toisella
// taulukolla, stringillä... esim items = 'Moro' olisi letillä mahdollinen

console.log(items);
console.log(items[3]);

// alkion arvoa voi muuttaa tai lisätä indeksiin viittaamalla
items[3] = 99;
console.log(items[3]);

items[9] = '10. alkion esimerkki'
console.log(items) // tyhjät alkiot näytetään "empty x4"
// jos tyhjän alkion yrittää console.logata, tulee "undefined"

// tulostetaan kaikki arvot yksitellen (uudehko tyyli)
console.log(items.length);
for (let i=0; i<items.length; i++) {
  console.log(items[i]);
}

// sama for-of:lla (vanha, tunnettu tyyli)
// voi käyttää const tai let riippuen tapauksesta
for (const item of items) {
  if(item) { // boolean, undefined olisi false eli if (item ! = undefined)
    console.log(item);
  }
}

// arraylle löytyy sisäänrakennettuja metodeja kuten sort (aakkosjärjestys)
// (ei toimi numeroille, koska sorttaa ne 1, 11, 2, 21, 333, 4)
// numeroita järjestäessä pitää antaa vertailusäännöt funktiolla:
// ages.sort((a,b) => a-b) pienimmästä suurimpaan => b-a suurimmasta pienimpään
const names = ['Frank', 'Scot', 'Bill', 'Alexander', 'Charles'];
names.sort();
console.log(names);
// names.reverse kääntää järjestyksen ympäri

// push ja pop ovat toistensa vastakohdat
// shift ja unshift ovat toistensa vastakohdat
// lisätään uusi nimi loppuun
names.push('Daniel');
// uusi nimi alkuun
names.unshift('Bob');
// pop poistaa
names.pop(); // poistaa viimeisen alkion
// jos arvo halutaan muuttujaan talteen: const muuttujaNimi = names.pop();
names.shift(); // poistaa ensimmäisen alkion

// löytyykö joku taulukosta? (true / false)
console.log(names.includes('Bill'));


// OBJEKTIT / OLIOT
// olioliteraali on tietorakenteena kuin pythonin sanakirja(dictionary)
// sisältö voi olla taas mitä vaan
const person = {name: 'Peppi', age: 15};
console.log('person-olio:', person)
person['age'] = 36; // muuttaa ominaisuuden arvon
person.name = 'Peppi Pitkätossu'; // muuttaa nimen  myös pistenotaatiolla
person.profession = 'student'; // lisää uuden ominaisuuden(property)
// tietyn ominaisuuden arvon hakeminen
console.log(person.name + ' on ' + person.age + '-vuotias.');

// metodin luominen olioon nimettömänä funktiona
const person2 = {
  name: 'Pekka Pouta',
  age: 100,
  pet: 'Sini',
  getinfo: function() {
    return this.name + ' on ' + this.age + '-vuotias.';
  },
};
console.log(person2.getinfo());


// FUNKTIOT
const name = 'Don Johnsson'
// kolme tapaa luoda funktioita
// jos funktio hakee parametriä ja sitä ei ole annettu, tulee sen tilalle
// undefined ja ohjelman suoritus jatkuu ongelmitta

// 1 'Klassinen'
function doSomething(name) {
  console.log('Perusfunktio',  name)
};
doSomething();

// 2 'Nimetön'
const doSomething2 = function(name){
  console.log('Funktio muuttujassa', name)
};
doSomething2()

// 3
const doSomething3 = () => {
  console.log('Uudehko fat arrow tyyli')
};
doSomething3()

// lottorivi (pallot 1-40) käärittynä funktioon
// palautetaan rivi taulukkona
// parametrit, jotta voi tehdä loton lisäksi viikkaria ja eurojackpotia
function getLotto(numberCount, maxValue) {
  const minunLottorivi = [];
  while (minunLottorivi.length < numberCount) {
    const number = Math.floor(Math.random() * maxValue + 1);
    if (!minunLottorivi.includes(number)) { // ei haluta samaa nro kahdesti
    minunLottorivi.push(number);
    }
    console.log('pallon arvo', number);
  }
  return minunLottorivi.sort((a, b) =>  b - a );
}
const myRow = getLotto(7, 40);
console.log(myRow);
console.log(getLotto(10,100));

// Luodaan lottokuponki, jossa n määrä rivejä
function luoLottoLappu(rivienlkm){
  const omaLottoLappu = [];
  for (let i=0; i<rivienlkm; i++); {
    getLotto(7,40);
    omaLottoLappu.push(myRow);
  }
  return omaLottoLappu
}
// 10 riviä lauantailottoa
const lauantaiLotto = luoLottoLappu(10);
console.log(lauantaiLotto);

// tulostetaan 10-rivin kupongin  ensimmäisen rivin 3.numero
console.log(lauantaiLotto[0][2]);

// VALUE SCOPE (ei päde var!)

// Muuttujan näkyvyys riippuu sen luomishetken sisennyksestä

// Aaltosulkeet luovat aina uuden sisemmän scopen, johon ei ulompaa näe

// Jos luodaan muuttujia "eri tasoilla", voi olla samannimisiä, mutta niihin
// päästään käsiksi aina vain samalla tai sisemmällä tasolla

// !!! Globaali arvo luodaan ilman sisennystä !!!


// Jatko-osa 20.11.2023
// TAULUKKO MUUTTUJAN PARAMETRINA

function arrayTest(numbers) {
  numbers.push(9);
  return numbers;
}
const numbers= [1,2,3];
console.log(arrayTest(numbers));
const numbers2 = numbers; // tehdään uusi muuttuja, joka viittaa samaan taulukkoon
let numbers3 = []; // huom. let eikä const
numbers3 = numbers3.concat(numbers); // luotiin uusi taulukko ja kopioitiin sinne toisen taulukon sisältö
// toinen tapa kopioida
const numbers4 = [...numbers];
// kolme pistettä(spread) purkaa arvot talukosta yksittäisiksi alkioiksi.
// Ilman niitä uuden muuttujan sisältö on array. [1,2,3,] => 1,2,3


