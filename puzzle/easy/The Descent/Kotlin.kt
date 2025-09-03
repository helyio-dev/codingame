import java.util.*
import java.io.*
import java.math.*

fun main(args : Array<String>) {
    val input = Scanner(System.`in`)

    while (true) {
        var maxH = -1
        var mountainToFire = 0
        for (i in 0 until 8) {
            val mountainH = input.nextInt()
            if (mountainH > maxH) {
                maxH = mountainH
                mountainToFire = i
            }
        }
        
        println(mountainToFire)
    }
}
