func sumDigits(_ n: Int) -> Int {
    return String(n).compactMap { Int(String($0)) }.reduce(0, +)
}

let R = Int(readLine()!)!
let C = Int(readLine()!)!
let T = Int(readLine()!)!

var visited = Array(repeating: Array(repeating: false, count: C), count: R)
var queue: [(Int, Int)] = []
var count = 0

if sumDigits(0) + sumDigits(0) <= T {
    queue.append((0, 0))
    visited[0][0] = true
    count = 1
}

let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while !queue.isEmpty {
    let (x, y) = queue.removeFirst()
    
    for (dx, dy) in directions {
        let nx = x + dx
        let ny = y + dy
        
        if nx >= 0 && nx < R && ny >= 0 && ny < C && !visited[nx][ny] {
            if sumDigits(nx) + sumDigits(ny) <= T {
                visited[nx][ny] = true
                queue.append((nx, ny))
                count += 1
            }
        }
    }
}

print(count)