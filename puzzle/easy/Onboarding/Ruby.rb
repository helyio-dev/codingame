STDOUT.sync = true

loop do
  enemy_1 = gets.chomp
  dist_1 = gets.to_i
  enemy_2 = gets.chomp
  dist_2 = gets.to_i

  if dist_1 < dist_2
    puts enemy_1
  else
    puts enemy_2
  end
end
