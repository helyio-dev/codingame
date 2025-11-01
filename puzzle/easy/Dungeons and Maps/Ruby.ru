w,h=gets.split.map(&:to_i)
sr,sc=gets.split.map(&:to_i)
n=gets.to_i
maps=[]
n.times do
  grid=[]
  h.times { grid << gets.chomp }
  maps << grid
end

def path_length(grid,sr,sc,h,w)
  r,c=sr,sc
  steps=0
  visited=Array.new(h){Array.new(w,false)}
  loop do
    return nil if r<0||r>=h||c<0||c>=w
    return nil if visited[r][c]
    visited[r][c]=true
    cell=grid[r][c]
    return steps+1 if cell=='T'
    return nil if cell=='.'||cell=='#'
    steps+=1
    case cell
    when '^' then r-=1
    when 'v' then r+=1
    when '<' then c-=1
    when '>' then c+=1
    else return nil
    end
  end
end

best_len=Float::INFINITY
best_idx=nil
maps.each_with_index do |g,i|
  l=path_length(g,sr,sc,h,w)
  if l && l<best_len
    best_len=l
    best_idx=i
  end
end

puts best_idx.nil? ? 'TRAP' : best_idx
