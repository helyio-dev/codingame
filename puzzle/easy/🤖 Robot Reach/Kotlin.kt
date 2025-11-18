import java.util.*
import java.io.*
import java.math.*

fun sumDigits(n: Int): Int {
    return n.toString().map { it - '0' }.sum()
}

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)
    val R = input.nextInt()
    val C = input.nextInt()
    val T = input.nextInt()

    val visited = Array(R) { BooleanArray(C) }
    val queue: Queue<Pair<Int, Int>> = LinkedList()
    var count = 0

    if (sumDigits(0) + sumDigits(0) <= T) {
        queue.add(0 to 0)
        visited[0][0] = true
        count++
    }

    val directions = arrayOf(0 to 1, 1 to 0, 0 to -1, -1 to 0)

    while (queue.isNotEmpty()) {
        val (x, y) = queue.poll()

        for ((dx, dy) in directions) {
            val nx = x + dx
            val ny = y + dy

            if (nx in 0 until R && ny in 0 until C && !visited[nx][ny]) {
                if (sumDigits(nx) + sumDigits(ny) <= T) {
                    visited[nx][ny] = true
                    queue.add(nx to ny)
                    count++
                }
            }
        }
    }

    println(count)
}