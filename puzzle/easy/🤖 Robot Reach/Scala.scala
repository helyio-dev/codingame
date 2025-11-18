object Solution {
  def sumDigits(n: Int): Int = {
    n.toString.map(_.asDigit).sum
  }
  
  def main(args: Array[String]): Unit = {
    val R = scala.io.StdIn.readInt()
    val C = scala.io.StdIn.readInt()
    val T = scala.io.StdIn.readInt()
    
    val visited = Array.ofDim[Boolean](R, C)
    val queue = scala.collection.mutable.Queue[(Int, Int)]()
    var count = 0
    
    if (sumDigits(0) + sumDigits(0) <= T) {
      queue.enqueue((0, 0))
      visited(0)(0) = true
      count += 1
    }
    
    val directions = Array((0, 1), (1, 0), (0, -1), (-1, 0))
    
    while (queue.nonEmpty) {
      val (x, y) = queue.dequeue()
      
      for ((dx, dy) <- directions) {
        val nx = x + dx
        val ny = y + dy
        
        if (nx >= 0 && nx < R && ny >= 0 && ny < C && !visited(nx)(ny)) {
          if (sumDigits(nx) + sumDigits(ny) <= T) {
            visited(nx)(ny) = true
            queue.enqueue((nx, ny))
            count += 1
          }
        }
      }
    }
    
    println(count)
  }
}