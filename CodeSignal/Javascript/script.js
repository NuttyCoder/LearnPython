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
// Equality and Strict Equality Operators (== and ===): The double equals operator (==) checks equality in value, 
// whereas the triple equals operator (===) checks equality in both value and type.

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

// The "if" Statement: Initiating Decision-Making
// Regard the if statement as the gatekeeper of conditionals. It definitively states, "If this is true, then perform this specific action". It’s comparable to choosing between chocolate and vanilla ice cream. Let’s take a closer look at an example:

let myScore = 100;
let friendScore = 80;
// If our score is higher, we get to brag about it!
if (myScore > friendScore) {
    console.log("Score bragging rights are mine!");
    console.log("Victory is sweet!");
}

console.log("Game over.");
// Note that in JavaScript, the conditions we inspect using if statement must always be wrapped in parentheses, like so: if (condition). The if statement applies to all statements within its block formed by braces ({}).

// In the above script, since myScore is greater than friendScore, both lines within the block are executed. If myScore was smaller than friendScore, they would not.

// Regardless of the condition's verdict, "Game over." is printed because it's situated outside the if block.

// The "else" Statement: Expanding Our Options
// Often, we're presented with multiple potential outcomes. For such instances, we utilize the else statement, to account for the "otherwise" scenario. Let's see it in action:

let myScore = 60;
let friendScore = 80;
// If our score is higher, we brag. Else, we console ourselves!
if (myScore > friendScore) {
    console.log("I scored higher!");
    console.log("Hurrah!");
} else {
    console.log("My friend scored higher. Well played.");
    console.log("I’ll come back stronger next time.");
}

console.log("Game over.");
// In this scenario, if the if statement's condition is met, the program executes only the block within the if statement. However, if the condition is false and thereby the first block is not executed, the program moves to execute the block within the else clause instead.

// Again, irrespective of the chosen path, "Game over." is always printed as it resides outside the conditionals’ realm.

//  The "else if" Statement: Handling Multiple Conditions
// There are occasions when we must consider several distinct conditions. This is where else if flourishes, lending nuanced control over multiple possibilities.

let myScore = 80;
let friendScore = 80;
// If our score is higher, we brag.
// If our score is lower, we console ourselves.
// If our scores are tied, we declare a stalemate.
if (myScore > friendScore) {
    console.log("I scored higher!");
} else if (myScore < friendScore) {
    console.log("Oh no, my friend scored higher!")
} else {
    console.log("It's a tie game!")
}
// The else if clause is checked only if the initial if statement is false. If the else if condition turns out to be true, its block of code will be executed. 
// However, if its condition is also false, the flow of the program will descend to any subsequent else if clauses, checking their conditions, 
// or to the else statement if there are no more else if clauses. The else block always executes as a fallback if none of the preceding conditions 
// in the if and else if clauses are met. As such, the program can follow a multitude of paths, offering you granular control over its operation.

// Understanding Logical Operators
// Logical operators in JavaScript allow us to evaluate multiple conditions. The && operator checks if both conditions are true, || checks if either one is true, and ! negates a condition.

let isWeekend = true;
let isHoliday = false;
let isSunny = false;

if (isWeekend && isSunny) {
  console.log("It's the weekend and it's sunny, let's go to the park!");
} else if (isHoliday && !isSunny) {
  console.log("It's a holiday but not sunny, let's go to the museum."); 
} else if (isWeekend || isHoliday) {
  console.log("It's either weekend or a holiday, let's decide based on the weather.");
} else {
  console.log("It's neither the weekend nor a holiday, let's stay at home.");
}

// Decide on a travel destination based on budget and weather conditions.
let budget = 1000; // Our travel budget in dollars
let weatherSunny = true; // The weather is sunny

if (budget >= 1500 && weatherSunny) {
  console.log("Let's book a beach vacation!");
} else if (budget < 1500 && weatherSunny) {
  console.log("Let's plan a camping trip in the mountains!");
} else {
  console.log("Let's stay home and save for a bigger trip next time.");
}


let weather = "sunny";
let onVacation = true;
let haveMoney = true; // We have money for the trip

// Now, check if it's sunny and we're on vacation
if (weather === "sunny" && onVacation && haveMoney) {
    console.log("Beach trip time!");
} else {
    console.log("No beach trip today.");
}


let weather = "sunny";
let budget = 150;

// Decide where to go based on weather and budget
if (weather === "sunny" && budget >= 150) {
    console.log("Let's go to the beach!");
} else if (weather === "rainy" || budget < 150) {
    console.log("How about visiting a museum?");
}

