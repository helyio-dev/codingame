package main

import (
	"fmt"
)

func charFromDist(dist int) byte {
	if dist >= 0 && dist <= 9 {
		return byte('0' + dist)
	}
	if dist >= 10 && dist <= 35 {
		return byte('A' + dist - 10)
	}
	return ' '
}

type Point struct {
	r, c int
}

func main() {
	var w, h int
	fmt.Scan(&w, &h)

	maze := make([][]byte, h)
	var startR, startC int
	
	for r := 0; r < h; r++ {
		var row string
		fmt.Scan(&row)
		maze[r] = []byte(row)
		for c, char := range maze[r] {
			if char == 'S' {
				startR, startC = r, c
			}
		}
	}

	dist := make([][]int, h)
	for r := 0; r < h; r++ {
		dist[r] = make([]int, w)
		for c := 0; c < w; c++ {
			dist[r][c] = -1 
		}
	}

	queue := []Point{}
	
	if maze[startR][startC] != '#' {
		dist[startR][startC] = 0
		queue = append(queue, Point{startR, startC})
	}

	dr := []int{0, 0, 1, -1}
	dc := []int{1, -1, 0, 0}

	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]

		for i := 0; i < 4; i++ {
			nextR, nextC := current.r + dr[i], current.c + dc[i]
			
			if nextR < 0 { 
				nextR += h
			} else if nextR >= h {
				nextR -= h
			}

			if nextC < 0 {
				nextC += w
			} else if nextC >= w {
				nextC -= w
			}

			
			if dist[nextR][nextC] == -1 && maze[nextR][nextC] != '#' {
				dist[nextR][nextC] = dist[current.r][current.c] + 1
				queue = append(queue, Point{nextR, nextC})
			}
		}
	}

	for r := 0; r < h; r++ {
		for c := 0; c < w; c++ {
			if maze[r][c] == '#' {
				fmt.Print("#")
			} else if dist[r][c] == -1 {
				fmt.Print(".")
			} else {
				fmt.Print(string(charFromDist(dist[r][c])))
			}
		}
		fmt.Println()
	}
}