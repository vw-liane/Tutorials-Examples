console.log('Hello World--OG'); // statement
// expresses action to be carried out
let my_name = "Leo"; // delcare var
console.log(my_name); // default val--undefined

// two ways declare multiple variables
let firstName, lastName;
let otherName = "They", theirName = "Other";

// BEST PRACTICE
let bestName = "name";
let superName = "visitor"

// constants ... value not change
// not need to reassign, best prac--use <CONSTANT>
const interestRate = 0.3;
// interestRate = 1; // error-reassignment
console.log(interestRate);

// dynamic binding
// type of variable determined at runtime based
// on value they assign
console.log(typeof my_name);
my_name = 45;
console.log(typeof my_name);

// can use same name for an attribute?
const name = 'first Name'; 
// ^^no error shown 

// making objects
const person = 
{ // OBJECT LITERAL
  // key-value pairs
  name: 'New Names', //COMMA
  age: 34,
  city: 'Cincinatti'
}; //semicolon here

console.log(person);  // dot is best choice
console.log("\nDot notation: ", person.age);

// bracket notation
console.log("Bracket notation: ", person['name'])

// however can use brackets for when property
// selected at runtime by user
let user_select = 'city' // input here
console.log("\nUser selection: ", user_select)
console.log("Selected-Output: ", person[user_select])

function greet(name) // parameters passed only used
{               // w/in function
  console.log('I greet you', name + '!');
  //             interesting comma makes space
  //             + makes no space
} // no semicolon
// BEHOLD later "template literals" for string printing

// call
greet('Barabbas');


// return
function square(num)
{
  return num * num;
}
let sqrd = square(2);
console.log(sqrd);    //another function, <log>
//      can take function-ARGUMENT as well