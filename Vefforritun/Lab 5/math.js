// Part 1: Node Module

// The ﬁrst function, called doDivision(a,b), shall return the result of a divided by b.
// The second function, called stringifyDivision(a,b), shall return a string describing the divison in the format "a divided by b is result". For example,stringifyDivision(4,2) shall return "4 divided by 2 is 2" (there is no need to anyhow round the result). stringifyDivision shall make use of doDivision. 


module.exports.doDivision = function (a,b) {
    var result = a / b;
    return result;
}


module.exports.stringifyDivision = function stringifyDivision (a,b) {
    var string = String(a) + " divided by " + String(b) + " is " + module.exports.doDivision(a,b);
    return string;
}