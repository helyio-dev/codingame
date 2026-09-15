w=gets.to_i+2;g=?#*w;gets.to_i.times{g<<?#<<gets}
s={}
while i=g=~/O/
q=*i;g[i]=?#
q.map{|j|[1,-1,w,-w].map{k=j+_1;g[k]==?O&&(q<<k;g[k]=?#)}}
q.map{s[_1]=q.size}
end
gets;$<.map{x,y=_1.split;p s[y.to_i*w+x.to_i-~w]||0}
