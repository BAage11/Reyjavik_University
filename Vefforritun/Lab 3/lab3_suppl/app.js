
/* Part I - CAPTCHA */
function mathProblem() {
    var num1;
    var num2;
    var operator;
    var taskMsg = document.getElementById("taskMsg");

    num1 = Math.floor((Math.random() * 11) + 1);
    num2 = Math.floor((Math.random() * 11) + 1);
    operators = [{ sign: "+",
                method: function(a,b){ return a + b; } },
                { sign: "-",
                method: function(a,b){ return a - b; } },
                { sign: "*",
                method: function(a,b){ return a * b; } }];

    var selectedOperator = Math.floor(Math.random()*operators.length);
    var operator = operators[selectedOperator].sign;                  
    //this will give the operator sign

    var answer = operators[selectedOperator].method(num1, num2);
    //this will give the answer

    var problem = "Calculate " + String(Math.max(num1, num2)) + String(operator) + String(Math.min(num1, num2));

    taskMsg.innerHTML = problem;
    return answer
}

answer = mathProblem()

function resetAll() {
    var user_input = document.getElementById("mathIn").value;
    var display_output = document.getElementById("resultMsg");

    display_output.className = ""
    display_output.style.display = "None"
    display_output.innerHTML = ""

    answer = mathProblem()
}

function evaluateResult() {
    var user_input = document.getElementById("mathIn").value;
    var display_output = document.getElementById("resultMsg");
    if (user_input == answer) {
        display_output.className = "alert alert-success";
        display_output.style.display = "block";
        display_output.innerHTML = "correct";
    } else {
        display_output.className = "alert alert-danger";
        display_output.style.display = "block";
        display_output.innerHTML = "incorrect";
    }

    setTimeout(resetAll, 5000);
}


/* Part II - Asynchronicity */
function printLoop() {
    var user_input_2 = document.getElementById("loopNumber").value;
    var result_output = document.getElementById("loopOutput")
    var text = ""
    result_output.innerHTML = ""

    var i;
    for (i = 1; i <= user_input_2; i++) {
        setTimeout(document.getElementById("loopOutput").innerHTML += i + "<br>", 10);
    }
} 