const n = parseInt(readline());
let value = 0; 
let value2 = 0; 
let screen = ""; 
let operation = ""; 

function updateValue() {
  if (operation == "+") {
    value += value2;
  } else if (operation == "-") {
    value -= value2;
  } else if (operation == "x") {
    value *= value2;
  } else if (operation == "/") {
    value /= value2;
  } else {
    value = value2;
  }
  value = Math.round(value * 1000) / 1000;
}

for (let i = 0; i < n; i++) {
  const key = readline();

  if (operation.length == 2 && key == "=") {
    operation = operation[0];
  } else if (operation.length == 2) {
    operation = "";
  }

  if (key == "+" || key == "-" || key == "x" || key == "/") {
    if (screen != "") {
      updateValue();
    }
    operation = key;
    screen = value.toString();
  }
  else if (key == "AC") {
    value = 0;
    value2 = 0;
    operation = "";
    screen = "0";
  }
  else if (key == "=") {
    updateValue(); 
    screen = value.toString(); 
    operation += "="; 
  }
  else {
    screen += key;
    value2 = parseInt(screen);
  }
  console.log(screen); 
  if (key == "+" || key == "-" || key == "x" || key == "/" || key == "AC" || key == "=") {
    screen = "";
  }
}