/*Understanding Variables
Think of a variable in JavaScript as a box. This box stores data that can be changed, accessed, and manipulated within a program. 
Variables are declared in two ways: let and const, each with its own characteristics:*/


let age = 20;
const year = 1900; // A constant. Its value can't change.

age = 21; // Variables created with let can be reassigned.

/*JavaScript Null and Undefined Types
In JavaScript, we frequently encounter situations in which a variable doesn't have a value. In such cases, the null and undefined types come into play.

Imagine you possess a flower jar (variable), but it's empty. There is no flower inside. This absence of content is what null in JavaScript represents — 
an intentionally empty or non-existent value.

Suppose you have a label for a candy jar, but you don't actually have the jar. 
This is where undefined comes in. It indicates that a variable has been declared, but doesn't yet hold any value.*/

let flowerJar = null;         // we have an empty flower jar
console.log(flowerJar);       // outputs: null

let candyJar;                 // we have a label for a candy jar, but no actual jar
console.log(candyJar);        // outputs: undefined

/*Naming Variables in JavaScript
Choosing good variable names makes your code easier to understand. When naming JavaScript variables, remember that:
They are case-sensitive.
They should be descriptive.
They can't start with a number.
They can contain only letters, numbers, $, and _.
Here are some good examples:*/
let myFavoriteColor;
let message1;
let $location;
/*Assignment Operators
Assignment operators assign values to variables. The most common operator is =, but JavaScript also includes +=, -=, *=, /=, and %=. Have a look:*/

let x = 10; // x is 10
x += 5; // adding 5 to x makes x 15
x -= 3; // subtracting 3 from x makes x 12
x *= 2; // multiplying x by 2 makes x 24

/*Dissecting Assignment and Equality Operators
--Assignment Operator (=): The assignment operator assigns a value to its left operand based on the value of its right operand.*/

let x = 5; // x is now 5
--Equality and Strict Equality Operators (== and ===): The double equals operator (==) checks equality in value, whereas the triple equals operator (===) checks equality in both value and type.

console.log(5 == '5'); // true
console.log(5 === '5'); // false
/* Inequality and Strict Inequality Operators (!= and !==): The double not equals operator (!=) checks for inequality in value, 
whereas the triple not equals operator (!==) checks for inequality in either value or type.*/

console.log(5 != '5'); // false
console.log(5 !== '5'); // true


// Store a number in a variable and then change the value using an assignment operator
let starsCount = 9;  // Number of stars in our own galaxy
starsCount *= 100;  // Now, starsCount is 900, as if we're imagining 100 galaxies!

console.log(starsCount);  // Let's see how many stars we have now!

// Declare a variable named 'planet' and set its initial value
let planet = "Earth"; 

// Using an assignment operator to update the value of 'planet'
// TODO: Add 2021 to the variable using an assignment operator
planet = "Earth" + "2021"; 

// Log the current value to the console
console.log(planet); // Output should be 'Earth2021'

// Cosmos and Astronomy
let planet = "Earth"; // Declaring a variable for our planet
console.log(planet); // Earth is our home in the cosmos

let numberOfMoons = 1;// Assignment: Earth has one moon
console.log("Does Earth == Mars?", planet == "Mars"); // Equality: comparing Earth to Mars, which should be false
console.log("Number of Earth's moons === 1:", numberOfMoons === 1); // Does Earth have one moon?

// Declaring a variable to store the number of planets in our solar system.
let numberOfPlanets = 8;

// TODO: Use strict equality to compare number of planets to the number 8 and log the result.
console.log(numberOfPlanets === '8'); 

// Declare a variable 'planet' and assign it the name of our home planet.
// TODO: Declare variable for planet
let planet = "Earth";
// Define a variable 'moons' to hold the moon status of our planet, which is currently unknown.
// TODO: Declare a variable for moons with a 'null' value
let moons = null;
// Write a variable 'galaxy' that will represent the galaxy's name, but it's not known yet.
// TODO: Declare a variable for a galaxy without defining a value
let galaxy;
// Now, compare the 'planet' using equality operators and print the results.
// TODO: Compare 'planet' with the string value of our home planet
console.log(planet === "Earth")
// TODO: Check if 'moons' has a value that is strictly 'null'
console.log(moons === null);
