'use strict';

const luvut = [];

for (let i = 0; i <= 4; i +=1) {
  const luku = parseInt(prompt('Anna luku: '));
  luvut.unshift(luku)
}

for (let i = 0; i < luvut.length; i++) {
  console.log(luvut[i])
}
