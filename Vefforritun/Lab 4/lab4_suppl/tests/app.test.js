// 1. For function doPythagoras(a,b)
describe('doPythagoras(a,b)', function() {
//    var a = document.getElementById("varA").value;
//    var b = document.getElementById("varB").value;
  
    it('a) Value returned should have two digits after the comma.', function() {
        var c = doPythagoras(2,2);
        c = c.toFixed(2);
        chai.expect(doPythagoras(2,2).toFixed(2)).to.equal(c);
    });

    it('b) Check if the value is negative or not.', function() {
        chai.expect(doPythagoras(2,2), 'Invalid numbers').to.be.at.least(0);
    });

    it('c) Check if input is not a number.', function() {
        chai.expect(doPythagoras('a','b'), "Invalid input").to.be.NaN;   
    });
});
//        Other error tests:
//   1)     chai.expect(c);                                             --> True
//   2)     chai.expect(doPythagoras(2,2)).to.be(c);                    --> False
//   3)     chai.expect(-52, 'Invalid numbers').to.be.at.least(0);      --> False
//   4)     chai.expect('asdf', 'Invalid input').to.be.a('number');     --> False



// 2. For function checkURL(ﬁlename)
describe('checkURL(filename)', function() {
    it('a) Check to see if a valid string and/or empty string has been passed in.', function() {
        var anURL = 'https://veff213-sudoku.herokuapp.com/test'
        var getURL = checkURL(anURL)
        chai.expect(anURL).to.not.be.empty;
        chai.expect(typeof(getURL), false).to.equal('boolean', true);
   });

   it('b) Check if the input given is a valid URL.', function() {
        var getURL = checkURL('https://veff213-sudoku.herokuapp.com/test')
        chai.expect(getURL, false).to.equal(true);

   });
});
//        Other error tests:
//   1)     chai.expect('').to.not.be.empty                                 --> False
//   2)     chai.expect(typeof(43), 'True').to.equal('string', 'False');    --> False



// 3. For function markAndResetInput(inputField)
describe('markAndResetInput(inputField)', function() {
    it('a) Shall not throw an exception when a null object or undefined object is passed in.', function() {
        var input = null
        var input2 = undefined
        chai.expect(input).to.be.null;
        chai.expect(input2).to.be.undefined;
    });
});
//        Other error tests:
//     1)   chai.expect("asdf").to.be.null;                                 --> False
//     2)   chai.expect(453).to.be.undefined;                               --> False



// 4. For function loadFileAsync(url, callback)
describe('loadFileAsync(url, callback)', function() {
    it('a) Call the callback with the required resource if proper URL is provided, and b) Call the callback with null if URL is invalid or HTTP request is not succesful.', function() {
        var inputField = 'https://veff213-sudoku.herokuapp.com/test';
        chai.expect(loadFileAsync(inputField), function(response) {
            var display = document.getElementById("displayDiv");
            if (response === null) {
                display.textContent = "File could not be found!";
            } else {
                display.textContent = response;
            };
        });
    }).to.not.equal(null);
});                 
    // can't have "done();" here because of callback ????
