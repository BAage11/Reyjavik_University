let myMod = require('../math');
const chai = require('chai');
const sinon = require('sinon');


/* 1. For function doDivision(a,b)

a) A single test asserting that the function returns the correct division result (to 2 digits after the comma) given two positive numbers. */
describe('doDivision_Part_1a', function() {
    it('should return the correct division result (to two digits after the comma) given two positive numbers.', function () {
        var a = 5;
        var b = 3;    
        chai.expect(myMod.doDivision(a,b).toFixed(2)).to.equal((a/b).toFixed(2));
        });
    });


/* 1. (b) Two tests testing two (different) corner or failure cases. Add a comment before each test stating what that case is and why it can be considered a corner or failure case. */
describe('doDivision_Part_1b_Test_1', function() {
    it('Check the corner case of doing division with floating numbers (instead of integers) and/or input is zero (0).', function () {
        var c = 0.00;
        var d = 4.56;    
        // Corner case where division is made with a null value and a floating numbers, instead of expected integers. Should give a correct result all the same, as long as the 'doDivision' function has been implemented correctly.
        chai.expect(myMod.doDivision(c,d).toFixed(2)).to.equal((c/d).toFixed(2));
        });
    });


describe('doDivision_Part_1b_Test_2', function() {
    it('Check the corner case of diving by a minus number.', function () {
        var e = -52;
        var f = 7;    
        // Corner case where division is done with a minus value, which should result in a correct result as long as the 'doDivision' function has been implemented correctly.
        chai.expect(myMod.doDivision(e,f).toFixed(2)).to.equal((e/f).toFixed(2));
        });
    });


describe('doDivision_Part_1b_Test_3', function() {
    it('Check the failure case of doing division with a string input.', function () {
        var g = "2q";
        var h = 7;
        // Failure case where a string is divided by a number, resulting in 'Not a Number' result - division function can not calculate a string and a number together.
        chai.expect(myMod.doDivision(g,h).toFixed(2)).to.equal('NaN');
    });
});


describe('doDivision_Part_1b_Test_4', function() {
    it('Check the failure case where input is null.', function () {
        var i = 2;
        var j = null;    
        // Failure case where division is made by zero, which returns an infite number (a number cannot be divided by zero).
        chai.expect(myMod.doDivision(i,j).toFixed(2)).to.equal('Infinity');
    });
});



/* 2. For function stringifyDivision(a,b)

(a) A single test asserting that the function returns the correct string("a divided by b is result") given two positive numbers. Use a Stub/Fake (using the Sinon module) to replace the call to the doDivision function. */
describe('stringifyDivision_Part_2', function() {
    var k = 6;
    var l = 8;

    beforeEach(() => {
        var fakeCheck = sinon.fake.returns(k/l);
        sinon.replace(myMod, 'doDivision', fakeCheck);
    });

    it('Testing that the function "stringifyDivision(a,b) returns the correct string, using a Stub/Fake (with Sinon module).', function () {
            chai.expect(myMod.stringifyDivision(k,l)).to.equal(String(k) + " divided by " + String(l) + " is " + String(k/l));
    });
});
