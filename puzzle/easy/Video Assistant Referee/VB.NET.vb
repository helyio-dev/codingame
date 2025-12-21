Imports System
Imports System.Linq
Imports System.Collections.Generic

Module Solution
    Class Player
        Public Property X As Integer
        Public Property Y As Integer
        Public Property IsActive As Boolean
    End Class

    Sub Main()
        Dim grid(14) As String
        For i As Integer = 0 To 14
            grid(i) = Console.ReadLine()
        Next

        Dim playersA As New List(Of Player)
        Dim playersB As New List(Of Player)
        Dim ballX As Integer = 0
        Dim ballY As Integer = 0
        Dim attacker As Char = " "c

        For y As Integer = 0 To 14
            For x As Integer = 0 To 50
                Dim c As Char = grid(y)(x)
                If c = "a"c Or c = "A"c Then
                    playersA.Add(New Player With {.X = x, .Y = y, .IsActive = (c = "A"c)})
                ElseIf c = "b"c Or c = "B"c Then
                    playersB.Add(New Player With {.X = x, .Y = y, .IsActive = (c = "B"c)})
                ElseIf c = "o"c Then
                    ballX = x : ballY = y : attacker = "A"c
                ElseIf c = "O"c Then
                    ballX = x : ballY = y : attacker = "B"c
                End If
            Next
        Next

        Dim offsideCount As Integer = 0
        Dim isVarOffside As Boolean = False

        If ballY > 0 And ballY < 14 Then
            If attacker = "A"c Then
                Dim limitX As Integer = playersB.Select(Function(p) p.X).OrderBy(Function(x) x).ElementAt(1)
                Dim offsides = playersA.Where(Function(p) p.X < 25 And p.X < ballX And p.X < limitX)
                offsideCount = offsides.Count()
                isVarOffside = offsides.Any(Function(p) p.IsActive)
            Else
                Dim limitX As Integer = playersA.Select(Function(p) p.X).OrderByDescending(Function(x) x).ElementAt(1)
                Dim offsides = playersB.Where(Function(p) p.X > 25 And p.X > ballX And p.X > limitX)
                offsideCount = offsides.Count()
                isVarOffside = offsides.Any(Function(p) p.IsActive)
            End If
        End If

        If offsideCount = 0 Then
            Console.WriteLine("No player in an offside position.")
        Else
            Console.WriteLine($"{offsideCount} player(s) in an offside position.")
        End If

        Console.WriteLine(If(isVarOffside, "VAR: OFFSIDE!", "VAR: ONSIDE!"))
    End Sub
End Module