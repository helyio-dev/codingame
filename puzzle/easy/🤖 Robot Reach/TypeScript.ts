function sumDigits(n: number): number {
    return n.toString().split('').map(Number).reduce((a, b) => a + b, 0);
}

const input = require('fs').readFileSync(0, 'utf-8').trim().split('\n');
const R: number = parseInt(input[0]);
const C: number = parseInt(input[1]);
const T: number = parseInt(input[2]);

const visited: boolean[][] = Array(R).fill(null).map(() => Array(C).fill(false));
const queue: [number, number][] = [];
let count: number = 0;

if (sumDigits(0) + sumDigits(0) <= T) {
    queue.push([0, 0]);
    visited[0][0] = true;
    count = 1;
}

const directions: [number, number][] = [[0, 1], [1, 0], [0, -1], [-1, 0]];

while (queue.length > 0) {
    const [x, y] = queue.shift()!;
    
    for (const [dx, dy] of directions) {
        const nx = x + dx;
        const ny = y + dy;
        
        if (nx >= 0 && nx < R && ny >= 0 && ny < C && !visited[nx][ny]) {
            if (sumDigits(nx) + sumDigits(ny) <= T) {
                visited[nx][ny] = true;
                queue.push([nx, ny]);
                count++;
            }
        }
    }
}

console.log(count);