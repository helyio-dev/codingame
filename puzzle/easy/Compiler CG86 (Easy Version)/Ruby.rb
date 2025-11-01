e = gets.split
ops = []
i = 0
if e[0] == '+' || e[0] == '-'
  ops << [(e[0] == '+' ? 'ADD' : 'SUB'), e[1].to_i]
  i = 2
else
  ops << ['ADD', e[0].to_i]
  i = 1
end

while i < e.size
  ops << [(e[i] == '+' ? 'ADD' : 'SUB'), e[i+1].to_i]
  i += 2
end

cnt = Hash.new(0)
ops.each { |op, v| cnt[[op,v]] += 1 }
done = {}

ops.each do |op,v|
  next if done[[op,v]]
  puts "REPEAT #{cnt[[op,v]]}" if cnt[[op,v]] > 1
  puts "#{op} cgx #{v}"
  done[[op,v]] = true
end
puts "EXIT"
