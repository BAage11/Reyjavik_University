
// Get the board from the backend, and call the function to display the board.
// If website is offline, call the function to display board with 'auto-made' board
function getAjax() {
    var paramValue = document.getElementById('difficultySelector').value;
    var url = 'https://veff213-sudoku.herokuapp.com/api/v1/sudoku';
    var board;

        axios.post(url, { difficulty: paramValue })
        .then(function(response) {
            board = response.data.board;
        })
        .catch(function(error) {
            board = autoBoard(paramValue);
        })
        .then(function () {
            displayBoard(board);
        });
};


// Displaying the board, retreiving one cell at a time and putting the element from the retreived (back-end) board to the displayed board. If value of the element is ".", then nothing is done to that particular cell.
function displayBoard(board) {
    clearBoard();
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            var cell = document.getElementById("cell"+String(i)+String(j));
            var element = board.boxes[i][j]

            if (element != ".") {
                cell.innerHTML = cell.value = element;
                cell.style.backgroundColor = "lightgrey";
                cell.disabled = true;
            }
        } 
    } 
};


// Function that clears the board each time the user pushes the 'Generate Sudoku' button, so a new board with new values can be made.
function clearBoard() {
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            var cell = document.getElementById("cell"+String(i)+String(j));
            cell.innerHTML = cell.value = '<input id="cell" type="number" min="1" max="9" style="background-color: white;">';
            cell.style.backgroundColor = "white"; 
        } 
    }
};  



// After the timeout is finished (5 seconds), the board is displayed as it previously was - that is colous implemented are put back to white. Should also be done to red-coloured cells, but have not yet been able to get to that function / operation because of other errors.
function resetAll() {
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            var cell = document.getElementById("cell"+String(i)+String(j));
            if (cell.value == "") {
                cell.style.backgroundColor = "white";                
            } else if (cell.value < 1) {
                cell.style.backgroundColor = "white";
            } else if (cell.value > 9) {
                cell.style.backgroundColor = "white";
            } else {
                cell.style.backgroundColor = "lightgrey";
            }
        }
    }
};


// When user clickes the 'Validation' button, this function retrieves information one cell at a time. If value is missing (empty cell), the background colour turns to yellow. This function should also display cells with 'wrong input' as red, but have not been able to implement that yet, because of other errors. At last, the function calls the 'resetAll' function to display the board as it was before the validation button was pushed. 
function checkValidation() {
    for (i = 0; i < 9; i++) {
        for (j = 0; j < 9; j++) {
            var cell = document.getElementById("cell"+String(i)+String(j));
            if (cell.value == "") {
                cell.style.backgroundColor = "yellow";                
            } else if (cell.value < 1) {
                cell.style.backgroundColor = "red";
            } else if (cell.value > 9) {
                cell.style.backgroundColor = "red";
            } else {
                cell.style.backgroundColor = "lightgrey";
            }
        } 
    } 
    setTimeout(resetAll, 5000);
};


// Automatic boards that will be displayed (in accordance to the chosen difficult level) if the server of the back-end is not currently working.
function autoBoard(value) {
    var Easy = {"boxes": [['5', '6', '4', '8', '7', '2', '3', '9', '1'],
                         ['.', '.', '3', '.', '1', '.', '.', '.', '.'],
                         ['2', '.', '1', '3', '9', '.', '.', '.', '5'],
                         ['4', '2', '9', '.', '.', '8', '7', '1', '3'],
                         ['6', '5', '7', '2', '3', '1', '8', '4', '9'],
                         ['3', '1', '8', '9', '4', '7', '5', '2', '6'],
                         ['.', '.', '6', '4', '2', '3', '.', '5', '8'],
                         ['.', '3', '5', '7', '8', '9', '2', '6', '4'],
                         ['8', '4', '2', '1', '.', '.', '9', '3', '7']] };

    var Medium = {"boxes": [['8', '7', '.', '4', '5', '.', '2', '1', '.'], 
                           ['.', '4', '.', '.', '2', '.', '8', '5', '.'], 
                           ['6', '2', '5', '.', '1', '.', '.', '9', '.'], 
                           ['7', '6', '.', '9', '3', '1', '5', '4', '8'], 
                           ['5', '.', '4', '8', '6', '2', '3', '.', '1'], 
                           ['.', '8', '.', '5', '.', '7', '9', '6', '2'], 
                           ['2', '.', '7', '.', '9', '4', '.', '.', '5'],
                           ['9', '5', '8', '6', '7', '3', '1', '.', '4'],
                           ['4', '.', '6', '2', '.', '5', '.', '.', '.']] }; 

    var Hard = {"boxes": [['4', '.', '.', '.', '.', '.', '5', '3', '9'],
                         ['9', '.', '.', '.', '4', '.', '6', '.', '1'],
                         ['.', '.', '.', '.', '.', '.', '7', '.', '4'],
                         ['.', '9', '6', '.', '7', '8', '2', '5', '3'],
                         ['.', '4', '7', '5', '.', '2', '9', '1', '6'],
                         ['.', '.', '.', '1', '9', '6', '8', '4', '7'],
                         ['.', '.', '1', '.', '8', '.', '4', '.', '2'],
                         ['.', '8', '4', '.', '.', '.', '3', '.', '5'],
                         ['2', '.', '.', '.', '5', '4', '1', '7', '8']] };
        
    if (value == 'easy') {
        return Easy;
    } else if (value == 'medium') {
        return Medium;
    } else {
        return Hard;
    };
};