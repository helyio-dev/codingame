let digit = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
let numberTen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
let tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
let powerOfTen = ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"];

const n = parseInt(readline());
for (let i = 0; i < n; i++) {
  let number = readline();
  let answer = "";
  if (Math.sign(number) == -1) {
    answer = "negative ";
    number = number.substring(1, number.length);
  }
  let split = getSplit(number); 
  let array = groupBy3(number, split); 
  console.error(array);
  for (let j = split - 1; j >= 0; j--) {
    if (parseInt(array[j][0]) > 0) {
      answer += digit[parseInt(array[j][0])] + " " + powerOfTen[0] + " ";
    }
    if (parseInt(array[j][1]) > 0) {
      if (parseInt(array[j][1]) == 1) {
        answer += numberTen[parseInt(array[j][2])] + " ";
      } else {
        answer += tens[parseInt(array[j][1]) - 2];
        if (parseInt(array[j][2]) > 0) {
          answer += "-" + digit[parseInt(array[j][2])] + " ";
        } else {
          answer += " ";
        }
      }
    } else {
      if (parseInt(array[j][2]) > 0 || number.length == 1) {
        answer += digit[parseInt(array[j][2])] + " ";
      }
    }
    if (j > 0 && (array[j][2] != 0 || array[j][1] != 0 || array[j][0] != 0)) {
      answer += powerOfTen[j] + " "; 
    }
  }
  answer = answer.substring(0, answer.length - 1);
  console.log(answer);
}
function groupBy3(n, split) {
  let reversedNumber = n.split("").reverse();
  let array = [];
  for (let j = 0; j < split; j++) {
    let str = j * 3 + 2 <= reversedNumber.length - 1 ? reversedNumber[j * 3 + 2] : "0";
    str += j * 3 + 1 <= reversedNumber.length - 1 ? reversedNumber[j * 3 + 1] : "0";
    str += reversedNumber[j * 3];
    array.push(str);
  }
  return array;
}
function getSplit(n) {
  let split = Math.floor(n.length / 3);
  if (n.length % 3 != 0) {
    split++;
  }
  return split;
}