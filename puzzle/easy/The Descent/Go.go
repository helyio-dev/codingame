package main

import "fmt"

func main() {
	for {
		var maxH int = -1
		var mountainToFire int = 0
		for i := 0; i < 8; i++ {
			var mountainH int
			fmt.Scan(&mountainH)
			if mountainH > maxH {
				maxH = mountainH
				mountainToFire = i
			}
		}
		fmt.Println(mountainToFire)
	}
}
