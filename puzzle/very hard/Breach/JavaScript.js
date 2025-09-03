const LOCKS_TYPES = ["ss_f", "ss_m", "ss_n", "ss_asc", "ss_con", "ss_colv", "rs_f", "rs_n", "rs_colv", "gs_m"];
const tableauPeriodiqueDesElements = {
  1: "H",  
  2: "He",  
  3: "Li", 
  4: "Be",
  5: "B", 
  6: "C", 
  7: "N", 
  8: "O", 
  9: "F", 
  10: "Ne",
  11: "Na",
  12: "Mg",
  13: "Al",
  14: "Si",
  15: "P", 
  16: "S", 
  17: "Cl",
  18: "Ar",
  19: "K", 
  20: "Ca",
  21: "Sc",
  22: "Ti",
  23: "V", 
  24: "Cr",
  25: "Mn",
  26: "Fe",
  27: "Co",
  28: "Ni", 
  29: "Cu", 
  30: "Zn", 
  31: "Ga", 
  32: "Ge", 
  33: "As", 
  34: "Se", 
  35: "Br", 
  36: "Kr", 
  37: "Rb", 
  38: "Sr", 
  39: "Y", 
  40: "Zr",
  41: "Nb",
  42: "Mo",
  43: "Tc",
  44: "Ru",
  45: "Rh",
  46: "Pd",
  47: "Ag",
  48: "Cd",
  49: "In",
  50: "Sn",
  51: "Sb",
  52: "Te",
  53: "I", 
  54: "Xe",
  55: "Cs",
  56: "Ba",
  57: "La",
  58: "Ce",
  59: "Pr",
  60: "Nd",
  61: "Pm",
  62: "Sm",
  63: "Eu",
  64: "Gd",
  65: "Tb",
  66: "Dy",
  67: "Ho",
  68: "Er",
  69: "Tm",
  70: "Yb",
  71: "Lu",
  72: "Hf",
  73: "Ta",
  74: "W", 
  75: "Re",
  76: "Os",
  77: "Ir",
  78: "Pt",
  79: "Au",
  80: "Hg",
  81: "Tl",
  82: "Pb",
  83: "Bi",
  84: "Po",
  85: "At",
  86: "Rn",
  87: "Fr",
  88: "Ra",
  89: "Ac",
  90: "Th",
  91: "Pa",
  92: "U", 
  93: "Np",
  94: "Pu",
  95: "Am",
  96: "Cm",
  97: "Bk",
  98: "Cf",
  99: "Es",
  100: "Fm",
  101: "Md",
  102: "No",
  103: "Lr",
  104: "Rf",
  105: "Db",
  106: "Sg",
  107: "Bh",
  108: "Hs",
  109: "Mt",
  110: "Ds",
  111: "Rg",
  112: "Cn",
  113: "Nh",
  114: "Fl",
  115: "Mc",
  116: "Lv", 
  117: "Ts", 
  118: "Og", 
};
const digits = [
  [" ++++ ", "+    +", "+    +", "+    +", "+    +", " ++++ "],
  [" ++++ ", "+++++ ", "  +++ ", "  +++ ", "  +++ ", " +++++"],
  [" +++++ ", "++   ++", " +  ++ ", "   ++  ", "  ++   ", "+++++++"],
  [" +++++ ", "++   ++", "    ++ ", "++   ++", " +++++ ", "       "],
  ["   ++++ ", " ++   ++", " ++   ++", "++++++++", "      ++", "      ++"],
  ["++++++", "+     ", "++++  ", "    + ", "    + ", "+++++ "],
  [" +++ ", "+    ", "++++ ", "+   +", "+++  ", "     "],
  ["++++++", "    ++", "   ++ ", "  ++  ", " ++   ", " +    "],
  [" ++ ", "+  +", " ++ ", "+  +", " ++ ", "    "],
  [" ++++ ", "+    +", " ++++ ", "    + ", "    + ", ""], //J'ai enlevé le dernier string car le '+' n'etait pas adhjacent au autre et mon algorithme de detection de contours ne le prennais pas en compte
];
const colors = {
  W: "GRAY",
  w: "WHITE",
  R: "RED",
  r: "LIGHT_RED",
  G: "GREEN",
  g: "LIGHT_GREEN",
  B: "BLUE",
  b: "LIGHT_BLUE",
  y: "YELLOW",
  o: "ORANGE",
  P: "PINK",
  p: "LIGHT_PINK",
  V: "VIOLET",
  v: "LIGHT_VIOLET",
  "?": "CORRUPT",
};
function ss_n(data) {
  function fibonacci(n) {
    if (n in cache) {
      return cache[n];
    }
    let term = fibonacci(n - 2) + fibonacci(n - 1);
    cache[n] = term;
    return term;
  }
  let input = data.match(/\d+/g);
  let start = parseInt(input[0]);
  let targetTherm = parseInt(input[input.length - 1]);
  let cache = { 1: start, 2: start };
  return fibonacci(targetTherm + 1);
}
function rs_n(data) {
  function arithmetique(terms, n) {
    const r = terms[1] - terms[0];
    let actualN = terms.length;
    let term = terms[actualN - 1];
    while (actualN != n) {
      term += r;
      actualN++;
    }
    return term;
  }
  const input = data.match(/\d+/g);
  const targetTerm = parseInt(input[input.length - 1]);
  const terms = [];
  for (let i = 0; i < input.length - 1; i++) {
    terms.push(parseInt(input[i]));
  }
  return arithmetique(terms, targetTerm + 1);
}
function ss_f(data) {
  function isLower(char) {
    return char == char.toLowerCase();
  }
  for (let i = 0; i < data.length; i++) {
    if (isLower(data[i])) {
      return data[i].charCodeAt(0) - "a".charCodeAt(0);
    }
  }
}
function rs_f(data) {
  return data[0].charCodeAt(0) - "a".charCodeAt(0);
}
function gs_m(data) {
  const input = data.match(/\d+/g);
  return tableauPeriodiqueDesElements[input[0]];
}
function ss_m(data) {
  for (const [key, value] of Object.entries(tableauPeriodiqueDesElements)) {
    if (value == data) {
      return key;
    }
  }
}
function ss_asc(data) {
  function detectionContour(ascii) {
    const indexHelper = [
      [-1, -1],
      [-1, 0],
      [-1, 1],
      [0, -1],
      [0, 1],
      [1, -1],
      [1, 0],
      [1, 1],
    ];
    const contours = [];
    const visited = new Array(ascii.length).fill(0).map((i) => new Array(ascii[i].length).fill(false));
    function isValid(x, y) {
      return y >= 0 && y < ascii.length && x >= 0 && x < ascii[y].length;
    }
    function dfs(x, y, contour) {
      if (!isValid(x, y) || visited[y][x] || ascii[y][x] == " ") {
        return;
      }
      visited[y][x] = true;
      contour.push([y, x]);
      for (let i = 0; i < indexHelper.length; i++) {
        let dy = indexHelper[i][0];
        let dx = indexHelper[i][1];
        dfs(x + dx, y + dy, contour);
      }
    }
    for (let y = 0; y < ascii.length; y++) {
      for (let x = 0; x < ascii[y].length; x++) {
        if (!visited[y][x] && ascii[y][x] == "+") {
          let c = [];
          dfs(x, y, c);
          contours.push(c);
        }
      }
    }
    return contours;
  }
  function getMinMaxX(contour) {
    let minX = Infinity;
    let maxX = -Infinity;
    for (let i = 0; i < contour.length; i++) {
      const c = contour[i];
      const x = c[1];
      if (x > maxX) {
        maxX = x;
      }
      if (x < minX) {
        minX = x;
      }
    }
    return [minX, maxX];
  }
  function checkDigit(matrix, digit) {
    for (let i = 0; i < matrix.length; i++) {
      if (digits[digit][i].trim() != matrix[i].join("").trim()) {
        return false;
      }
    }
    return true;
  }
  const contours = detectionContour(data);
  let answer = "";
  for (let iContour = 0; iContour < contours.length; iContour++) {
    const contour = contours[iContour];
    const [minX, maxX] = getMinMaxX(contour);
    const matrix = new Array(data.length).fill(0).map(() => new Array(maxX - minX).fill(" "));
    for (let i = 0; i < contour.length; i++) {
      const y = contour[i][0];
      const x = contour[i][1] - minX;
      matrix[y][x] = "+";
    }
    for (let i = 0; i <= 9; i++) {
      if (checkDigit(matrix, i)) {
        answer += i;
      }
    }
  }
  return answer;
}
let last = false;
let count = 0;
function ss_con(data) {
  const input = data.match(/¬[^¬]+\.\.\./g);
  for (let i = 0; i < input.length; i++) {
    if (input[i][1] == "r") {
      console.error(i);
      if (i == 0) {
        if (count != 9) {
          count++;
          return 1;
        } else {
          count = 0;
          return 0;
        }
      }
      if (i == 5) {
        return 0;
      }
      return i + 1;
    }
  }
  return 0;
}
function ss_colv(data) {
  const input = data.match(/¬[A-Za-z]\+/g);
  console.error(input);
  return colors[input[0][1]];
}
function rs_colv(data) {
  return colors[data[1]];
}
while (true) {
  const lines = parseInt(readline());
  let lockType = null;
  let data = [];
  for (let i = 0; i < lines; i++) {
    const line = readline();
    console.error(line);
    if (lockType == null) {
      for (const _lockType of LOCKS_TYPES) {
        if (line.indexOf(_lockType) != -1) {
          lockType = _lockType;
        }
      }
      continue;
    }
    data.push(line);
  }
  switch (lockType) {
    case "ss_n":
      console.log(ss_n(data[0]));
      break;
    case "rs_n":
      console.log(rs_n(data[0]));
      break;
    case "ss_f":
      console.log(ss_f(data[0]));
      break;
    case "rs_f":
      console.log(rs_f(data[0]));
      break;
    case "gs_m":
      console.log(gs_m(data[0]));
      break;
    case "ss_m":
      console.log(ss_m(data[0]));
      break;
    case "ss_asc":
      console.log(ss_asc(data));
      break;
    case "ss_con":
      console.log(ss_con(data[0]));
      break;
    case "ss_colv":
      console.log(ss_colv(data[0]));
      break;
    case "rs_colv":
      console.log(rs_colv(data[0]));
      break;
  }
}