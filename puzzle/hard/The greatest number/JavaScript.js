const N = parseInt(readline());
let input = readline().split(" ");
let isNegatif = input.indexOf("-") != -1;
let haveDot = input.indexOf(".") != -1;
input.sort((a, b) => {
  if (a == "-") {
    return -1;
  } 
  else if (b == "-") {
    return 1;
  } 
  if (isNegatif) {
    if (a == ".") {
      return -1;
    } 
    if (b == ".") {
      return 1;
    }
    return a - b; 
  } else {
    if (a == ".") {
      return 1;
    } 
    if (b == ".") {
      return -1;
    }
    return b - a; 
  }
});
if (haveDot) {
  if (isNegatif) {
    input[1] = input[2]; 
    input[2] = "."; 
  } 
  else {
    input[input.length - 1] = input[input.length - 2];
    input[input.length - 2] = "."; 
  }
}
let answer = parseFloat(input.join(""));
if (answer == 0) {
  answer = 0;
}
console.log(answer);