def beats(a,b)
  { 'C'=>%w[P L], 'P'=>%w[R S], 'R'=>%w[C L], 'L'=>%w[S P], 'S'=>%w[C R] }[a].include?(b)
end

n = gets.to_i
num, sign, opp = [], [], []
n.times do
  a,b = gets.split
  num << a.to_i
  sign << b
  opp << []
end

idx = (0...n).to_a
while idx.size > 1
  nxt = []
  idx.each_slice(2) do |i1,i2|
    if beats(sign[i1],sign[i2])
      w,l = i1,i2
    elsif beats(sign[i2],sign[i1])
      w,l = i2,i1
    else
      w,l = num[i1] < num[i2] ? [i1,i2] : [i2,i1]
    end
    opp[w] << num[l]
    nxt << w
  end
  idx = nxt
end

w = idx[0]
puts num[w]
puts opp[w].join(' ')
