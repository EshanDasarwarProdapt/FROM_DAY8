// Primitive datatype

// 1. String
let name = "Alice";
console.log(name);          // Alice
console.log(typeof name);   // string

// 2. Number
let age = 25;
console.log(age);           // 25
console.log(typeof age);    // number

// 3. BigInt
let bigNumber = 123456789012345678901234567890n;
console.log(bigNumber);
console.log(typeof bigNumber); // bigint

// 4. Boolean
let isStudent = true;
console.log(isStudent);        // true
console.log(typeof isStudent); // boolean

// 5. Undefined
let city;
console.log(city);             // undefined
console.log(typeof city);      // undefined

// 6. Null
let car = null;
console.log(car);              // null
console.log(typeof car);       // object (this is a historical quirk)

// 7. Symbol
let uniqueId = Symbol("id");
console.log(uniqueId);         // Symbol(id)
console.log(typeof uniqueId);  // symbol


let student = {
    name: "Eshan",
    age: 22
};

let colors = ["Red", "Blue"];

function greet(){
    console.log("Hello")
}

greet ()