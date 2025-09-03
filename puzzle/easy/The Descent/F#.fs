open System

while true do
    let mutable maxH = -1
    let mutable mountainToFire = 0

    for i in 0 .. 8 - 1 do
        let mountainH = int(Console.In.ReadLine())
        if mountainH > maxH then
            maxH <- mountainH
            mountainToFire <- i
        
    printfn "%d" mountainToFire
    ()
