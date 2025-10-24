for(N=readline(),G={},S=new Set(),i=0;i<N;i++){a=readline().split` `.map(Number);(G[a[0]]||=[]).push(a[1]);S.add(a[0]);S.add(a[1])}
m={};f=u=>m[u]??(m[u]=G[u]?1+Math.max(...G[u].map(f)):1)
console.log(Math.max(...[...S].map(f)))
