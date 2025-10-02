var inputs = readline().split(" ");
const width = parseInt(inputs[0]);
const height = parseInt(inputs[1]);
const count = parseInt(readline());
let grid = [];
for (let i = 0; i < height; i++) {
  const raster = readline();
  grid.push(raster);
}
for (let z = 0; z < count; z++) {
  let g = [];
  for (let i = 0; i < grid[0].length; i++) {
    g.push([]);
    for (let j = 0; j < grid.length; j++) {
      g[i].push(0);
    }
  }
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      g[j][i] = grid[i][j];
    }
  }
  grid = g;
  for (let i = g.length - 1; i >= 0; i--) {
    for (let j = 0; j < g[0].length; j++) {
      if (grid[i][j] == ".") {
        for (let k = i - 1; k >= 0; k--) {
          if (grid[k][j] == "#") {
            grid[i][j] = "#";
            grid[k][j] = ".";
            break;
          }
        }
      }
    }
  }
}
for (let i = 0; i < grid.length; i++) {
  console.log(grid[i].join(""));
}