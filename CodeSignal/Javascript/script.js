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

let weather = "sunny";
let budget = 150;

// TODO: Write an 'if' statement to check if the weather is lovely and we have enough funds for a beach trip.
if (weather === 'sunny' && budget > 100)
    console.log("Yah! Let's go to the beach!");
else {
// Hint: The beach trip requires 'weather' to be "sunny" and 'budget' to be greater than 100.

console.log("Hmm, let's plan something else.");
}

// TODO: Declare a variable for your travel budget
let travelBudget = 1000;
// TODO: Declare a variable for the price of your trip ticket
let ticketPrice = 700;
// TODO: Declare a variable for the cost of special services
let specialServicesCost = 200;
if (travelBudget >= (ticketPrice + specialServicesCost)) {
    console.log("Your budget covers both the ticket price and special services.");
} else if (traveBudget >= ticketPrice) {
    console.log("Your budget price covers the ticket only, but not the special services.");
} else {
    console.log("Your budget does not cover the ticket price.");
}
// TODO: Write an if-else statement that first checks if your budget covers both the ticket price and the special services cost. If not, it should then check if the budget covers at least the ticket price.


//--------------------------------------------------------------------------------------------------------------------------------------------------------------

// ------------>  Introducing Functions
// In JavaScript, a function is a block of reusable code designed to perform a specific task when invoked or 'called'. 
// Consider a scenario in which we need to compute something or create a pop-up notification every time a user clicks on a button. 
// In such situations, we would enclose the necessary code within a function and invoke it whenever the button is clicked.

// Here is an example of defining a function named sayHello:
// a function to say hello
function sayHello() {
  // code inside here runs when the function is called
  console.log("Hello, world!");
}
// In this function, named sayHello, we print "Hello, world!" to the console when the function is invoked or called.

// You have learned to define or declare a straightforward function in JavaScript. This is the initial building block in creating reusable code blocks.

//--------->  Invoking Functions
// To utilize a function, we have to invoke or 'call' it by appending parentheses () to the function's name. This process resembles joining a teleconference using a unique meeting link. Just as you join the meeting only when you click the link, the code inside the function is executed only when the function is called.

// Let's invoke our sayHello function:


sayHello();  // Invokes the function, outputting: "Hello, world!"
// Here, sayHello(); is a function call informing JavaScript to execute the code block within the sayHello function.

// ------------------------------>  The Role of Parameters in Functions
// Parameters provide a function with its inputs, significantly enhancing the function's reusability. It's akin to injecting some intelligence into a function, creating a lightbulb moment. Consider a function that calculates the area of a circle. Such a function would only be useful if it could compute the area for any circle, regardless of its radius, and not just for a circle with a fixed radius.
// Observe the following function that greets a person using their name:
// a function that greets a person by name
function greetPerson(name) {
  console.log("Hello, " + name + "!");
}

// invoking the function with "Alice" as an argument
greetPerson("Alice");  // Outputs: "Hello, Alice!"
// In this function, name is a parameter. When we invoked greetPerson("Alice");, the value "Alice" was passed as an argument to the function.

// You've learned about bestowing a function with intelligence through parameters, making the function versatile and broadly applicable.

// ---------------------------------> Understanding Return Statements
// The return keyword acts like the conveyor belt in a factory line, which delivers the final product after all the operations are performed on the assembly line.

// Here's an example where we return the square of a number:
// function that returns the square of a number
function square(number) {
  return number * number; // number is the function parameter
}

const squaredNumber = square(5);
console.log(squaredNumber);  // Outputs: 25
// In this function, the square of 5 is returned, yielding 25 as the output.

// Through the return keyword, you've just learned how to make a function execute a calculation and deliver the result in JavaScript.

// --------------------------------->  Scope of Variables in Functions
// When a variable is declared within a function, it's only known within that function and cannot be accessed from outside. 
// This concept is similar to your home WiFi network; it can only be accessed when you are within its range.
// global variable
let globalVariable = "I'm global!";  // This is like a cellular network available everywhere

// function to check scope
function checkScope() {
  // local variable
  let localVariable = "I'm local!";  // This is like your home WiFi network
  console.log(globalVariable);  // Outputs: "I'm global!"
  console.log(localVariable);  // Outputs: "I'm local!"
}

checkScope();

console.log(globalVariable);  // Outputs: "I'm global!"
console.log(localVariable);  // Returns an error as localVariable is not defined outside the function
// In this code, localVariable is only accessible within checkScope(), while globalVariable can be accessed from anywhere in the code.

// We learned about variable scopes in JavaScript. Their concept is quite similar to the coverage of your home WiFi network versus a cellular network 
// that is available everywhere.

// a function to greet a planet by name
function greetPlanet(planetName) {
  return "Hello, " + planetName + "! Welcome to the cosmic party.";
}

// calling the greet function with "Mars" as a parameter
const greeting = greetPlanet("Mars"); 
console.log(greeting);  // Outputs a friendly greeting to Mars

// function that calculates the area of a circle
function circleArea(radius, pi) {
    return pi * radius * radius; // Use the passed pi value
}

// The radius of the moon's circle in the cosmos
const moonRadius = 1737.1; // in kilometers
const accuratePi = 3.141592653589793;
console.log("The area of the moon's circle is: " + circleArea(moonRadius, accuratePi) + " square kilometers.");  // Outputs the area of the moon's circle with a message

// Function to calculate a new weight based on different gravity
function calculateNewWeight(weight) {
  const gravityRatio = 0.38;
  return weight * gravityRatio;  // Apply the gravity ratio
}


// Using the function to calculate a weight of 70 units in a new environment
console.log(calculateNewWeight(70));  // Outputs the new weight

// TODO: Declare a function that greets travelers with the name of their planet as a parameter
//       and writes a greeting to the console.
function greetPlanetTraveler(planetName) {
    console.log(`Greetings, traveler from planet ${planetName}! Welcome to the cosmic community.`);
}
greetPlanetTraveler("Mars"); // Customize the greeting for a traveler from Mars
greetPlanetTraveler("Venus"); // And for Venus

// TODO: Define a function that takes a name as a parameter and returns a greeting message including the name.
function createGreeting (name) {
    return `Hello, ${name}! Welcome to the adventure!`;
}
// TODO: Invoke the function with a name of your choice and store the return value in a variable.
let greetingMessage = createGreeting("Heather")
// TODO: Use console.log to print out the variable containing the greeting.
console.log(greetingMessage);

//--------------------------------> JavaScript Arrays: A Closer Look
// An array in JavaScript is a collection of values or data that you access with an index, a number referring to a position in the array. 
// Imagine all the seats in a cinema theatre are numbered, and you're looking for seat number 10. This number, "10", is like the array index. In JavaScript, array indexing starts with 0. This is known as zero-based indexing. This means that the first element in the array is found at index 0, the second element is found at index 1 and so on. For example, consider the following array of rainbow colors:

let rainbowColors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"];
console.log(rainbowColors[0]); // Outputs "Red"

// Creating and Modifying Arrays
// Arrays in JavaScript are containers that can hold various data types. You can include data in an array during its creation or even after it has been created. This is akin to how you can pack a lunchbox with different types of food while making lunch, or even add more items later.


let variedArray = ["Hello", 25, true]; // The `variedArray` contains three different types of data.
// To modify an item in the array, select the compartment you want to modify and replace it with a new item:


let fruits = ["Apple", "Banana", "Mango"];
fruits[1] = "Grape";  // "Banana" is now "Grape"
console.log(fruits[1]); // Outputs "Grape"

// -----------> Accessing Array Length
// You can also find out how many compartments (elements) are in the lunchbox (array) using the .length property:


let colors = ["Red", "Green", "Blue"];
console.log(colors.length); // Outputs 3


// ------------------------------------>  Manipulating Arrays: A Basic Glimpse
// JavaScript provides various methods to help us manage items in the lunchbox, such as adding or removing items. 
// Today, we will cover two basic methods: .push(), which adds an element, and .pop(), which removes the last element:

let colors = ["Red", "Green", "Blue"];
colors.push("Yellow");  // Yellow added
console.log(colors);  // Output: ["Red", "Green", "Blue", "Yellow"]
colors.pop();  // Yellow removed
console.log(colors);  // Output: ["Red", "Green", "Blue"]


// We have an array of movie genres for a cinema theatre
let movieGenres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi"];
console.log(movieGenres[2]); // Output the third genre: "Drama"

// Let's change "Horror" to "Adventure" and add "Fantasy" at the end
movieGenres[3] = "Adventure";
movieGenres.push("Fantasy");
console.log(movieGenres); // Outputs: ["Action", "Comedy", "Drama", "Adventure", "Sci-Fi", "Fantasy"]

let confirmedGuests = ["Alice", "Bob", "Charlie"];
confirmedGuests[2] = "Eva"; // Replacing "Charlie" with new name
console.log("We have " + confirmedGuests.length + " guests coming to the movie night:");
console.log(confirmedGuests);


// Array representing the seats reservation status in a cinema row
let cinemaSeats = [false, true, false, true, false];

// A new person tries to book the third seat
cinemaSeats[2] = true;

// Let's check if the third seat is now booked
console.log("Which seats are booked?", cinemaSeats);


// Let's pretend we are organizing a cinema seating plan using arrays!
let cinemaSeats = ["Empty", "Empty", "Empty", "Empty", "Empty"];

// TODO: Add a command to book seat number 3
cinemaSeats[2] ="Booked";
console.log(cinemaSeats[2]); // Outputs "Booked"

// Now, let's find out how many seats we have in our cinema.
console.log(cinemaSeats.length); // Outputs 5

// TODO: Create an array of movie titles in a cinema, e.g., "Space Adventure", "Ocean's Mystery".
let movies = ["Space Adventure", "Ocean's Mystery", "Mountain Tales"];
// TODO: Remove the last movie title from the movies array
movies.pop();
// TODO: Add a new movie title to the end of the movies array
movies.push("Galaxy Voyage")
// TODO: Display the updated list of movies in the console
console.log("Updated movies list:", movies)

// ---------------------------------->Introduction and Topic Overview
// Welcome to the universe of JavaScript! Today's topic is JavaScript Objects, a pivotal concept in JavaScript and programming! 
// Objects efficiently group related data and functions.

// In terms analogous to the real world, consider JavaScript Objects as school report cards that consolidate your subject scores 
// (data) and remarks (characteristics) in one place. The objective of our lesson is to help you master JavaScript Objects to 
// manage related data and functions effectively. Let's begin!

// An Object in JavaScript, mirroring real-world entities, includes two principal components: properties and methods. 
// Imagine there's a car, it displays certain characteristics, dubbed as properties (like color, make, and model), and some actions, 
// labeled as methods (like start, stop). Essentially, JavaScript Objects package related data (properties) and functions (methods).

// ------------------------------> JavaScript Object Syntax
// Let's define a JavaScript Object employing object literal syntax. Using our car example, let's frame a JavaScript Object:

let car = {
    color: 'red',
    make: 'Toyota',
    model: 'Corolla',
};
// The object car contains three properties: color, make, and model, defined using the 'key': 'value' syntax, separated by commas (,), enclosed within curly braces ({}).

// To access properties, we can employ dot notation (.) or bracket notation ([]):

let carColor1 = car.color; // 'red', access using dot notation
let carColor2 = car['color']; // 'red', access using bracket notation


// ------> Properties of JavaScript Objects
// JavaScript Object properties describe the object. For our car object, the properties are color, make, and model. You can add, modify, and delete properties as follows:


car.color = 'blue'; // modifying color property
car.roofRack = true; // adding roofRack property
delete car.roofRack; // removing roofRack property
// Properties in JavaScript can sport special names, enclosed by quotes or bracket notation:


let house = {
    'number of rooms': 4,
    1: 'one',
};

let rooms = house['number of rooms']; // equals 4
let one = house[1]; // equals 'one'

Methods in JavaScript Objects
Methods, the second component of JavaScript Objects, encapsulate actions or behaviors. In our car object, methods might include actions, like start, stop, accelerate, and brake. Methods are defined as functions within an object:

JavaScript
Copy to clipboard
Play
let car = {
    color: 'red',
    make: 'Toyota',
    model: 'Corolla',
    start: function() {
        return 'Engine started!';
    },
    displayColor: function() {
        // you can access Object properties by using 'this' keyword
        console.log('The color of the car is ' + this.color); // prints "The color of the car is red"
    }
};

let carStart = car.start(); // calls the start method and returns 'Engine started!'
// Pay attention that here we use a slightly modified version of function creation called function expression. Namely, instead of this:


function start() {
    return 'Engine started!';
}
// we use the following notation:


start: function() {
    return 'Engine started!';
}
//  If we needed to provide parameters to the function, we would include the parameters in the parentheses after the function keyword:

start: function(key) {
    if (key === 'correct') {
        return 'Engine started!';
    }
}
// and would call like this: car.start('correct');

// -----------------> Creating and Using JavaScript Objects
//  Moving forward, let's compose and use our own JavaScript Objects and manage the properties dynamically:


let user = {
    name: 'John',
    age: 30,
};

let userName = user.name; // 'John'
let userAge = user['age']; // 30

user.isAdmin = true; // a new property 'isAdmin' is added
user.introduce = function() { // a new method is added
    console.log("Hi, I am " + this.name);
}
delete user.age; // deletes the 'age' property
// JavaScript supports dynamic alteration of properties, setting it apart from several other programming languages.

let car = {
    brand: 'Honda',
    model: 'Civic',
    year: 2022,
    displayInfo: function() {
        // This function returns the car information as a string
        return this.brand + ' ' + this.model + ' (' + this.year + ')';
    }
};

let carInfo = car.displayInfo();
console.log(carInfo); // 'Honda Civic (2022)'

let car = {
    brand: 'Tesla',
    model: 'Model 3',
    drive: function() {
        return "Vroom vroom!";
    }
};

// Changing the model and adding a new property.
car.color = 'white';
car.model = 'Model Y';

// TODO: Call the 'drive' method here and print the result
console.log(car.drive());

let car = {
    brand: 'Ford',
    model: 'Mustang',
    startEngine: function() {
        console.log('Vroom!');
    }
};

// Let's change the car color to 'black'
car.color = 'black';

// Now let's try to start the engine of the car
car.startEngine(); // This should output: Vroom! But it doesn't. Oh no!

// Define an object representing a car
let car = {
    color: 'blue',
    maxSpeed: 120,
    honk: function() {
        return 'Beep beep';
    }
    // TODO: Add a method to enable the car to honk
};
car.color ='green';
// Use the car object: Change the color and honk the horn
// TODO: Update the car's color to 'green'
let hornSound = car.honk(); // Call the honk method
console.log(hornSound);

// TODO: Define a car object with properties 'make', 'model', and 'year'
let car = {
    make: 'Toyota',
    model: 'Corolla',
    year: 2021,

// TODO: Add a method to the car object that logs a message with the car's details
    displayDetails: function () {
        console.log(`This car is a ${this.year}  ${this.make} ${this.model}.`);
    }
};
// TODO: Call the method to display the car's information
car.displayDetails();

// ---------------------------------------->> Introduction to JavaScript ES6+ Features
// Welcome to an engaging session on JavaScript ES6+! JavaScript ES6+ marks an evolution from the original JavaScript language - 
// the ECMAScript standard. Debuting as ECMAScript 2015 (ES2015 or ES6) and continuing with subsequent releases (ES7, ES8, ES9, and so on), 
// ES6+ has provided a rich set of advanced features and syntax improvements. These enhancements have streamlined coding practices, 
// making JavaScript more concise, efficient, and readable. Today, you will master these transformative features: Arrow functions, 
// Spread operator, Destructuring, and Template strings. Through the use of practical examples, you will learn how these features 
// revolutionize the process of writing efficient JavaScript code.

// Arrow Functions — A New Way to Define Functions
// The Arrow functions offer a modern twist to JavaScript. They facilitate a shorter and cleaner function notation than traditional JavaScript functions. Here's how you can use the => operator in functions with different numbers of parameters to define arrow functions:

// Arrow Function with No Parameters

const greet = () => "Hello, World!";
// This function does not take any arguments and returns the string "Hello, World!". Its equivalent in traditional function definition would look like this:


function greet() {
    return "Hello, World!";
}
// Arrow Function with One Parameter

const addFive = num => num + 5;
// This function that takes a single argument num and adds 5 to it. The equivalent traditional function definition is:


function addFive(num) {
    return num + 5;
}
// Arrow Function with Two or More Parameters

const multiply = (a, b) => a * b;
// This function takes two arguments, a and b, and returns their product. Its equivalent traditional function definition would be:


function multiply(a, b) {
    return a * b;
}
// All three variations demonstrate how arrow functions provide a more concise and clean syntax as compared to traditional function definitions.

// The Spread Operator (…) — Simplifying Array and Object Manipulation
// The Spread operator offers intuitive solutions for managing arrays and objects. It facilitates copying arrays, adding elements to arrays, and copying objects. Here's how:

const fruits = ['apple', 'banana', 'orange'];
const moreFruits = [...fruits, 'peach', 'pear'];  // This operation copies the `fruits` array and adds 'peach' and 'pear'
console.log(moreFruits); // prints ['apple', 'banana', 'orange', 'peach', 'pear']

const user = { name: 'John', age: 21 };
const admin = { ...user, role: 'admin' };  // This operation copies the `user` object and adds `role: 'admin'`
console.log(admin); // prints { name: 'John', age: 21, role: 'admin' }
// The Spread operator simplifies array and object management, leading to more readable code.


// Destructuring — Making Multiple Assignments Easier
// Destructuring in JavaScript is a crucial tool that allows you to unpack values from arrays and properties from objects into distinct variables. Let's explore this with an example:


const rgb = [255, 200, 0];
const [red, green, blue] = rgb;  // Array destructuring
console.log(red); // prints 255
console.log(green); // prints 200

const rgbObj = {red: 255, green: 200, blue: 0};
const {red, green, blue} = rgbObj;  // Object destructuring
console.log(red); // prints 255
console.log(green); // prints 200
// Destructuring provides clear, readable assignments, enhancing code readability.
//- ------------------------------------>>Template Strings — Easier String Interpolation
// Template strings simplify string interpolation significantly. Use backticks (``) to define template strings, and then embed expressions within ${ }.

// Here's an example:


let greet = 'Hello';
let name = 'John';
// Here, we're embedding `greet` and `name` variables within a template string
let message = `${greet}, ${name}! How are you today?`;
console.log(message); // prints "Hello, John! How are you today?"
// Using template strings saves time on string manipulation, thereby enhancing the readability of the code.

// In situations where you have multiple elements to combine into a single string with the same separator, JavaScript's array.join(separator) 
// method can be extremely beneficial.

// The join method operates on an array and accepts a separator as a parameter. This separator is placed between each element of the array 
// as they're joined into a single string. If a separator isn't provided, a comma , is used by default.

// Let's consider a practical example:

const fruitNames = ['Apple', 'Banana', 'Cherry'];
const fruitList = fruitNames.join(', ');

console.log(fruitList);  // Outputs: "Apple, Banana, Cherry"
// In this example, fruitNames is an array containing individual fruit names. Calling join(', ') on fruitNames consolidates 
// all the fruits into a single string, each separated by , . This is particularly useful when dealing with multiple elements that 
// require the same separator. It effectively simplifies the task of merging elements and enhances the readability of the code.

// Recipe Book using ES6+ features
const combineIngredients = (ingredient1, ingredient2, ...rest) => {
  console.log(`Mixing ${ingredient1} and ${ingredient2} with additional ingredients: ${rest.join(', ')}`);
// The rest.join(', ') operation creates a string from the elements of the array rest by concatenating them with a given separator ', '
};

const [mainIngredient, secondaryIngredient, ...additionalIngredients] = ['flour', 'water', 'salt', 'yeast'];
combineIngredients(mainIngredient, secondaryIngredient, ...additionalIngredients);

// Define a recipe using an arrow function with destructuring and template strings
const recipeMessage = ({name, servings, ingredient1, ingredient2, ingredient3}) => {
  return `To make ${servings} servings of ${name}, you will need ${ingredient1}, ${ingredient2}, ${ingredient3}`;
};

// Use the arrow function and spread operator to add a twist
const basicRecipe = {name: 'Peanut Butter Cookies', servings: 4, ingredient1: 'peanut butter', ingredient2: 'sugar'};
const twistRecipe = {...basicRecipe, ingredient3: 'chocolate chips'};/* use spread operator to copy the basicRecipe object and create a new object with ingredient3 added to it */ ;
console.log(recipeMessage(twistRecipe)); // Should print the recipe with the twist ingredient

// Recipe ingredients and a function to combine them into a baking mixture
const ingredients = { flour: '1 cup', sugar: '1/2 cup', eggs: 2 };
// Incorrectly using parameters instead of destructuring
const mixIngredients = ({flour, sugar, eggs}) => `Mix ${flour}, ${sugar} and ${eggs} eggs to make a mixture.`;

// The function call is not passing the ingredients as separate arguments when it should be destructuring an object
const recipeMessage = mixIngredients(ingredients);
console.log(recipeMessage); // Output is not as expected due to a code bug

// A simple recipe manager

// Destructuring an array of ingredients
const ingredients = ['flour', 'sugar', 'eggs', 'butter'];
// TODO: Assign ingredient variables using array destructuring
const [ingredient1, ingredient2, ingredient3, ingredient4] = ingredients;
// TODO: Use a template string to create a message about the main ingredients for a cake
const message = `The main ingredients for the cake are: ${ingredient1}, ${ingredient2}, ${ingredient3},and ${ingredient4}.`
// An arrow function to log the message
const logIngredients = () => console.log(message);

// Call the function to log the ingredients message
logIngredients();

// TODO: Define an arrow function named 'bakeCake' that takes in an array of ingredients and returns a string detailing the cake's ingredients. Use the `.join` method
const bakeCake =(ingredients) => `To bake a cake, you will need" ${ingredients.join(',')}.`;
// TODO: Create a constant array 'ingredients' with cake ingredients: 'flour', 'sugar', 'eggs', 'butter'
const ingredients = ['flour', 'sugar', 'eggs', 'butter'];
// TODO: Use destructuring to create variables from the 'ingredients' array, each representing an ingredient
const[ingredient1, ingredient2, ingredient3,ingredient4] = ingredients;
// TODO: Write a template string in 'bakingMessage' to describe the process using those 4 ingredient variables and print it to the console
const bakingMessage = `The key ingredients for your cake are ${ingredient1}, ${ingredient2}, ${ingredient3} and ${ingredient4}.`;
console.log(bakingMessage);
// TODO: Use 'console.log' to output the result of calling 'bakeCake'
console.log(bakeCake(ingredients));
