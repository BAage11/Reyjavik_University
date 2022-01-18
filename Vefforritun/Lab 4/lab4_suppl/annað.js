// 1. ForfunctiondoPythagoras(a,b)

chai.expect('doPythagoras()')

var assert = Noderequire('chai').assert;      // var assert = Noderequire('assert');
var app = Noderequire('../app');
var a = document.getElementById("varA");
var b = document.getElementById("varB");

describe('Calculation Output', function() {
    it('Value returned should have two digits after the comma.', function(){
      let result = app.doPythagoras(a,b);
      chai
      assert.equal(result, result.tofixed(2));
    });

    it('check to see if a number is negative.', function() {
      assert.isBelow(a, 0, 'Negative numbers')
    });

    it('check to see if a number is negative.', function() {
      assert.isBelow(b, 0, 'Negative numbers')
    });

    it('check to see if input is a number.', function() {
      assert.isNumber(a, 'Invalid input')
    });

    it('check to see if input is a number.', function() {
      assert.isNumber(b, 'Invalid input')
    });
  });



// 2. For function checkURL(ﬁlename)
// (a) The function shall return false whenever a variable that is not a string or an empty string is passedin. 
// (b) The function shall return true if a proper URL is passed in.

var inputURL = document.getElementById('fname')

describe('Check URL', function() {
    it('Check if the URL is a valid string.', function() {
        assert.isString(inputURL);
    });

    it('Check if the URL is a proper URL.', function() {
        assert.
    })

});




// 3. For function markAndResetInput(inputField)
// (a) The function shall not throw an exception/error when a null object or undeﬁned is passed in.





// 4. For function loadFileAsync(url,callback) 
// (a) The function shall call the callback with the required resource if a proper URL is provided
// (b) The function shall call the callback with null in case the URL is invalid or the HTTP request is not successful
