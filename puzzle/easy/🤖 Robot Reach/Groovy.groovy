def sumDigits(n) {
    n.toString().collect { it.toInteger() }.sum()
}

input = new Scanner(System.in);

R = input.nextInt()
C = input.nextInt()
T = input.nextInt()

def visited = new boolean[R][C]
def queue = []
def count = 0

if (sumDigits(0) + sumDigits(0) <= T) {
    queue << [0, 0]
    visited[0][0] = true
    count = 1
}

def directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

while (!queue.isEmpty()) {
    def (x, y) = queue.remove(0)
    
    directions.each { dx, dy ->
        def nx = x + dx
        def ny = y + dy
        
        if (nx >= 0 && nx < R && ny >= 0 && ny < C && !visited[nx][ny]) {
            if (sumDigits(nx) + sumDigits(ny) <= T) {
                visited[nx][ny] = true
                queue << [nx, ny]
                count++
            }
        }
    }
}

println count