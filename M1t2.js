// Write a program that prompts for user's name and then greets the user.
// Print the result to the HTML document: Hello, Name!

'use strict';
const fillName= document.querySelector('#kysyName');

const name = prompt('Kerro nimesi: ');

kysyName.innerHTML = `Hello ${name}!`;
