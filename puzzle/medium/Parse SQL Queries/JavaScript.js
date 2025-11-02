const sqlQuery = readline();
const ROWS = parseInt(readline());
const tableHeader = readline().split(" ");
let select = getSelect();
let from = getFrom();
let where = getWhere();
let orderBy = getOrderBy();
let data = [];
for (let i = 0; i < ROWS; i++) {
  const tableRow = readline();
  data.push(tableRow.split(" "));
}
writeTableName();
executeQuery();
function getSelect() {
  let tab = sqlQuery.substring(7, sqlQuery.indexOf("FROM") - 1).split(", ");
  let tab2 = [];
  if (tab[0] == "*") {
    for (let i = 0; i < tableHeader.length; i++) {
      tab2.push(getTableHeaderIndex(tableHeader[i]));
    }
  } else {
    for (let i = 0; i < tab.length; i++) {
      tab2.push(getTableHeaderIndex(tab[i]));
    }
  }
  return tab2;
}
function getFrom() {
  if (sqlQuery.indexOf("WHERE") != -1) {
    return sqlQuery.substring(sqlQuery.indexOf("FROM") + 5, sqlQuery.indexOf("WHERE") - 1);
  } else if (sqlQuery.indexOf("ORDER BY") != -1) {
    return sqlQuery.substring(sqlQuery.indexOf("FROM") + 5, sqlQuery.indexOf("ORDER BY") - 1);
  } else {
    return sqlQuery.substring(sqlQuery.indexOf("FROM") + 5);
  }
}
function getWhere() {
  let index = sqlQuery.indexOf("WHERE");
  if (index != -1) {
    let tab = [];
    if (sqlQuery.indexOf("ORDER BY") != -1) {
      tab = sqlQuery.substring(index + 6, sqlQuery.indexOf("ORDER BY") - 1).split(" = ");
    } else {
      tab = sqlQuery.substring(index + 6).split(" = ");
    }
    tab[0] = getTableHeaderIndex(tab[0]);
    return tab;
  }
  return null;
}
function getOrderBy() {
  let index = sqlQuery.indexOf("ORDER BY");
  if (index != -1) {
    let tab = sqlQuery.substring(index + 9).split(" ");
    tab[0] = getTableHeaderIndex(tab[0]);
    return tab;
  }
  return null;
}
function getTableHeaderIndex(str) {
  for (let i = 0; i < tableHeader.length; i++) {
    if (tableHeader[i] == str) {
      return i;
    }
  }
  return -1;
}
function writeTableName() {
  let str = "";
  for (let i = 0; i < select.length; i++) {
    str += tableHeader[select[i]] + " ";
  }
  console.log(str.slice(0, -1));
}
function executeQuery() {
  let dataE = []; 
  for (let i = 0; i < data.length; i++) {
    let line = []; 
    if (where) {
      if (data[i][where[0]] == where[1]) {
        for (let j = 0; j < select.length; j++) {
          line.push(data[i][select[j]]); 
        }
        dataE.push(line.join(" ")); 
      }
    } else {
      for (let j = 0; j < select.length; j++) {
        line.push(data[i][select[j]]); 
      }
      dataE.push(line.join(" ")); 
    }
  }
  if (orderBy) {
    let index = 0;
    for (let i = 0; i < select.length; i++) {
      if (select[i] == orderBy[0]) {
        index = i;
      }
    }
    dataE.sort(function (a, b) {
      let tabA = a.split(" "); 
      let tabB = b.split(" ");
      let value1 = tabA[index];
      let value2 = tabB[index];
      if (isNumeric(value1)) {
        value1 = +tabA[index];
        value2 = +tabB[index];
      }
      if (orderBy[1] == "DESC") {
        if (value1 > value2) {
          return -1;
        }
        return 1;
      } else {
        if (value1 > value2) {
          return 1;
        }
        return -1;
      }
    });
  }
  console.log(dataE.join("\n"));
}
function isNumeric(val) {
  return /^-?\d+$/.test(val);
}