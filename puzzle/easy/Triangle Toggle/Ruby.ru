hi, wi = gets.split.map(&:to_i)
style = gets.chomp
n = gets.to_i
triangles = n.times.map { gets.split.map(&:to_i) }
grid = Array.new(hi) { Array.new(wi, '*') }

def point_in_triangle(px, py, t)
  sign = ->(x1,y1,x2,y2,x3,y3){ (x1-x3)*(y2-y3)-(x2-x3)*(y1-y3) }
  d1 = sign[px,py,*t[0..3]]
  d2 = sign[px,py,*t[2..5]]
  d3 = sign[px,py,t[4],t[5],t[0],t[1]]
  !( [d1,d2,d3].any?{|v| v<0} && [d1,d2,d3].any?{|v| v>0} )
end

triangles.each do |t|
  (0...hi).each do |y|
    (0...wi).each do |x|
      grid[y][x] = grid[y][x]=='*' ? ' ' : '*' if point_in_triangle(x,y,t)
    end
  end
end

grid.each do |row|
  puts style=="expanded" ? row.join(" ") : row.join
end
