open System

let token = (Console.In.ReadLine()).Split [|' '|]
let  LX = int(token.[0])
let  LY = int(token.[1])
let mutable TX = int(token.[2])
let mutable TY = int(token.[3])

while true do
    let remainingTurns = int(Console.In.ReadLine())

        if (TY > LY) then
               printf("N")
                      TY <- TY - 1
                          elif (TY < LY) then
                                 printf("S")
                                        TY <- TY + 1

                                            if (TX > LX) then
                                                   printf("W")
                                                          TX <- TX - 1
                                                              elif (TX < LX) then
                                                                     printf("E")
                                                                            TX <- TX + 1

                                                                                printfn("")
                                                                                    ()