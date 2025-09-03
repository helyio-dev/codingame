import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)

    while (true) {
        val enemy1 = input.next()
        val dist1 = input.nextInt()
        val enemy2 = input.next()
        val dist2 = input.nextInt()

        if (dist1 < dist2) {
            println(enemy1)
        } else {
            println(enemy2)
        }
    }
}
