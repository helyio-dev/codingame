open System

while true do
    let enemy1 = Console.In.ReadLine()
    let dist1 = int (Console.In.ReadLine())
    let enemy2 = Console.In.ReadLine()
    let dist2 = int (Console.In.ReadLine())
    
    if dist1 < dist2 then
        printfn "%s" enemy1
    else
        printfn "%s" enemy2
    ()
