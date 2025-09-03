const EMPTY = 0;
const TILE_SPAWN_PROBABILITIES = [0.9, 0.1]; 

function evaluateBoard(board) {
    let score = 0;
    for (let row of board) {
        for (let tile of row) {
            score += tile;
        }
    }
    return score;
}

function getPossibleMoves(board) {
    const moves = [];
    return moves;
}

function makeMove(board, move) {
    return newBoard;
}

function spawnTile(board) {
    const emptyCells = [];
    for (let i = 0; i < 4; i++) {
        for (let j = 0; j < 4; j++) {
            if (board[i][j] === EMPTY) {
                emptyCells.push({ x: i, y: j });
            }
        }
    }
    const randomCell = emptyCells[Math.floor(Math.random() * emptyCells.length)];
    const newTileValue = Math.random() < TILE_SPAWN_PROBABILITIES[1] ? 4 : 2;
    board[randomCell.x][randomCell.y] = newTileValue;
}

function expectimax(board, depth, maximizingPlayer) {
    if (depth === 0) {
        return evaluateBoard(board);
    }

    const possibleMoves = getPossibleMoves(board);
    if (maximizingPlayer) {
        let maxEval = -Infinity;
        for (let move of possibleMoves) {
            const newBoard = makeMove(board, move);
            spawnTile(newBoard); 
            const eval = expectimax(newBoard, depth - 1, false);
            maxEval = Math.max(maxEval, eval);
        }
        return maxEval;
    } else {
        let totalEval = 0;
        const emptyCells = getEmptyCells(board);
        for (let cell of emptyCells) {
            const newBoard = [...board];
            newBoard[cell.x][cell.y] = 2; 
            totalEval += expectimax(newBoard, depth - 1, true) * TILE_SPAWN_PROBABILITIES[0];

            newBoard[cell.x][cell.y] = 4; 
            totalEval += expectimax(newBoard, depth - 1, true) * TILE_SPAWN_PROBABILITIES[1];
        }
        return totalEval / emptyCells.length; 
    }
}

while (true) {
    const seed = parseInt(readline()); 
    const score = parseInt(readline());
    const board = [];
    for (let i = 0; i < 4; i++) {
        const inputs = readline().split(' ').map(Number);
        board.push(inputs);
    }

    const bestMove = getBestMove(board);
    console.log(bestMove); 
}

function getBestMove(board) {
    const possibleMoves = getPossibleMoves(board);
    let bestScore = -Infinity;
    let bestMove = 'U';

    for (let move of possibleMoves) {
        const newBoard = makeMove(board, move);
        spawnTile(newBoard); 
        const score = expectimax(newBoard, 3, true); 
        if (score > bestScore) {
            bestScore = score;
            bestMove = move; 
        }
    }
    return bestMove;
}
