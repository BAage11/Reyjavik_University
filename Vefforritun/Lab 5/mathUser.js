// Part 1: Node Module

// The second ﬁle, mathUser.js, shall import the module and demonstrate its functionality by calling the two functions and printing their return values to the console. It is suﬃcient to call each function once (with arbitrary values).

var mymodule = require('./math.js');
var a = 4;
var b = 2;

console.log(mymodule.doDivision(a,b));
console.log(mymodule.stringifyDivision(a,b));