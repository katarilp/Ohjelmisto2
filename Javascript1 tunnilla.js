'use strict';
console.log('Tervehdys ulkoisesta tiedostosta!')

// 14.11. Matin opetus

// switch: huomaa breakit! Jos breakin jättää pois, se tulostaa kaiken pätevästä
// vaihtoehdosta loppuun saakka. Uppercasen voi laittaa myös promptin sulkeen
// ja puolipisteen jälkeen, jolloin se tallentuu muuttujaan.
const cabinClass = prompt("Enter the cabin class (A/B/C).");
cabinClass.toUpperCase(); // a --> A, mutta uutta arvoa ei sijoiteta muuttujaan
// jos haluaisi tallentaa (cabinClass = cabinClass.toUpperCase();) pitäisi olla let, eikä const
switch (cabinClass) { //tähän voisi myös laittaa switch (cabinClass.toUpperCase) {
  case 'A':
  case 'a':
    console.log('Top deck cabin with window.');
    break;
  case 'B':
    console.log('Top deck cabin without window.');
    break;
  case 'C':
    console.log('Windowless cabin under the car deck.');
    break;
  default:
    console.log("Invalid cabin class.");
}
// ^ break hypäyttää ohjelman jatkumisen tänne


// Toistorakenteet eli silmukat (loops: while ja for)
// loopeissa const toimii, jos se on olemassa vain yhden kierroksen verran
// while (true/false), pyörii, jos ehto on tosi (varo ikuista looppia)
let counter = 0;
while (counter < 5) {
  console.log('tämä ehto oli tosi', counter) // jos laittaa ...tosi' + counter)
  // tulostuu ...tosi4' kun kaksi stringiä yhdistetään. pilkulla tulee ' ...tosi 4'
  counter++; // sama kuin counter +1
}

// heitetään noppaa niin kauan että tulee 6
let gameOver = false;
while(!gameOver) {
  const noppa = Math.floor(Math.random() * 6 + 1)
  //arvotaan numro väliltä 0-0,999, kerrotaa 6 , lisätään 1 ja floor pyöristää alaspäin
  // Math.ceil(Math.random() * 6); pyöristäisi ylöspäin, mutta voisi tulla 0
  console.log('noppa', noppa)
  if (noppa === 6){
  gameOver = true;
  }
}

// for-silmukka
for (let i = 0; i<10; i++) {
  console.log('for-silmukan i arvo:', i);
}

// lottorivi (pallot 1-40)
for (let i= 0; i < 7; i++) {
  const number = Math.floor(Math.random() * 40 +1);
  console.log(i+1, 'pallon arvo', number)
}


// do/while -loop
// "tehdään ensin ja tarkistetaan sitten"
// käytetään harvoin, koska yleensä saman saa tehtyä whilella

// whilen korvaaminen forilla--> for(;;) {annetaan ehto ja pyörii niin kauan}
// ^Matin mielestä ruma tapa. Ei mitään syytä käyttää koskaan!