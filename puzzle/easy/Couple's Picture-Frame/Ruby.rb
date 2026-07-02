wife = gets.chomp
husband = gets.chomp

width = wife.size.lcm(husband.size)

wife = wife * (width/wife.size).floor
husband = husband * (width/husband.size).floor

puts wife
husband.chars.zip(wife.chars).each{|char1 , char2| puts char1 + " "*(width-2) + char2}
puts husband