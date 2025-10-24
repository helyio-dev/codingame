[l,H]=readline().split` `.map(Number)
g=[];for(i=0;i<H;i++)g.push(readline())
m=[];for(n=0;n<20;n++)m[n]=g.map(x=>x.slice(n*l,n*l+l))
map={};m.forEach((x,i)=>map[x.join``]=i)
R=()=>{s=+readline();l=[];for(i=0;i<s;i++)l.push(readline());d=[];for(i=0;i<s;i+=H)d.push(l.slice(i,i+H).join``);v=0;for(j of d)v=v*20+map[j];return v}
a=R();b=R();o=readline();r=Math.floor(eval(a+o+b))
if(!r)console.log(m[0].join`\n`)
else{out=[];while(r)out.push(r%20),r=Math.floor(r/20);i=out.length;while(i--)for(j=0;j<H;j++)console.log(m[out[i]][j])}
