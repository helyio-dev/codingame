Module Player
    Sub Main ()
        While True
            Dim enemy1 as String = Console.ReadLine()
            Dim dist1 as Integer = Integer.Parse(Console.ReadLine())
            Dim enemy2 as String = Console.ReadLine()
            Dim dist2 as Integer = Integer.Parse(Console.ReadLine())

            If dist1 < dist2 Then
                Console.WriteLine(enemy1)
            Else
                Console.WriteLine(enemy2)
            End If
        End While
    End Sub
End Module
