let sumDigits n =
    string n |> Seq.map (string >> int) |> Seq.sum

let r = stdin.ReadLine() |> int
let c = stdin.ReadLine() |> int
let t = stdin.ReadLine() |> int

let visited = Array2D.create r c false
let mutable count = 0

let directions = [|(0,1);(1,0);(0,-1);(-1,0)|]

let queue = System.Collections.Generic.Queue<int * int>()

if sumDigits 0 + sumDigits 0 <= t then
    queue.Enqueue(0,0)
    visited.[0,0] <- true
    count <- count + 1

while queue.Count > 0 do
    let (x,y) = queue.Dequeue()
    
    for (dx,dy) in directions do
        let nx = x + dx
        let ny = y + dy
        
        if nx >= 0 && nx < r && ny >= 0 && ny < c && not visited.[nx,ny] then
            if sumDigits nx + sumDigits ny <= t then
                visited.[nx,ny] <- true
                queue.Enqueue(nx,ny)
                count <- count + 1

printfn "%d" count