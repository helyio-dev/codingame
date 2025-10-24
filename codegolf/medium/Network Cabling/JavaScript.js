for(N=+readline(),X=[],Y=[],i=0;i<N;i++){a=readline().split` `;X.push(+a[0]);Y.push(+a[1]);}
X.sort((a,b)=>a-b);Y.sort((a,b)=>a-b);
m=Y[N>>1];console.log(X[N-1]-X[0]+Y.reduce((s,y)=>s+Math.abs(y-m),0))