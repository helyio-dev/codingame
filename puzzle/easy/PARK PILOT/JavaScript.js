const N = parseInt(readline()); 
let needLength = true;
let calculLSide = [];
let data = [];
let carLength;
let consecutiveR0 = 0;
let consecutiveL0 = 0;
let availableSpace = [];
for (let i = 0; i < N; i++) {
  const sensorData = readline().split(""); 
  data.push({
    FL: sensorData[0],
    FR: sensorData[1],
    BR: sensorData[2],
    BL: sensorData[3],
  });
  if (needLength) {
    if (calculLSide.length == 0) {
      if (data[i].FL == 0) {
        calculLSide = ["L", i];
      } else if (data[i].FR == 0) {
        calculLSide = ["R", i];
      }
    } else {
      if (calculLSide[0] == "L") {
        if (data[i].BL == 0) {
          carLength = i - calculLSide[1] + 1;
          needLength = false;
        }
      } else {
        if (data[i].BR == 0) {
          carLength = i - calculLSide[1] + 1;
          needLength = false;
        }
      }
    }
  }
  if (data[i].FL == 0) {
    consecutiveL0++;
    if (consecutiveL0 == carLength) {
      availableSpace.push(i + carLength - 1 + "L"); 
      consecutiveL0--;
    }
  } else {
    consecutiveL0 = 0;
  }
  if (data[i].FR == 0) {
    consecutiveR0++;
    if (consecutiveR0 == carLength) {
      availableSpace.push(i + carLength - 1 + "R"); 
      consecutiveR0--;
    }
  } else {
    consecutiveR0 = 0;
  }
}
console.log(carLength);
for (let i = 0; i < availableSpace.length; i++) {
  console.log(availableSpace[i]);
}