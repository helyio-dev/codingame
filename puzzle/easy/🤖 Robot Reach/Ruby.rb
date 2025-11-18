def sum_digits(n)
  n.to_s.chars.map(&:to_i).sum
end

r = gets.to_i
c = gets.to_i
t = gets.to_i

visited = Array.new(r) { Array.new(c, false) }
queue = []
count = 0

if sum_digits(0) + sum_digits(0) <= t
  queue << [0, 0]
  visited[0][0] = true
  count = 1
end

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

while !queue.empty?
  x, y = queue.shift
  
  directions.each do |dx, dy|
    nx = x + dx
    ny = y + dy
    
    if nx >= 0 && nx < r && ny >= 0 && ny < c && !visited[nx][ny]
      if sum_digits(nx) + sum_digits(ny) <= t
        visited[nx][ny] = true
        queue << [nx, ny]
        count += 1
      end
    end
  end
end

puts count