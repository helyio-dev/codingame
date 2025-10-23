package main

import (
	"fmt"
	"math"
)

func main() {
	var W,H,t1,t2,t3 int
	fmt.Scan(&W,&H,&t1,&t2,&t3)
	p1,p2:=map[byte][2]int{},map[byte][2]int{}
	for y:=0;y<H;y++{
		var a,b string
		fmt.Scan(&a,&b)
		for x:=0;x<W;x++{
			if a[x]!='.'{p1[a[x]]=[2]int{x,y}}
			if b[x]!='.'{p2[b[x]]=[2]int{x,y}}
		}
	}
	res:=make([][]byte,H)
	for i:=range res{
		res[i]=make([]byte,W)
		for j:=range res[i]{res[i][j]='.'}
	}
	for k,v:=range p1{
		x1,y1:=v[0],v[1]
		x2,y2:=p2[k][0],p2[k][1]
		x3:=int(math.Floor(float64(x1) + float64(x2-x1)*float64(t3-t1)/float64(t2-t1)))
		y3:=int(math.Floor(float64(y1) + float64(y2-y1)*float64(t3-t1)/float64(t2-t1)))
		if x3>=0&&x3<W&&y3>=0&&y3<H{
			if res[y3][x3]=='.'||k<res[y3][x3]{res[y3][x3]=k}
		}
	}
	for _,r:=range res{fmt.Println(string(r))}
}
