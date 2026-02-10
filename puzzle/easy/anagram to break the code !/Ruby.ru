def is_anagram(w1, w2)
  s1 = w1.downcase
  s2 = w2.downcase
  return false if s1 == s2
  s1.chars.sort == s2.chars.sort
end

w = gets.chomp
s = gets.chomp

words = s.scan(/[a-zA-Z]+/)
key_index = words.find_index { |word| is_anagram(w, word) }

if key_index.nil?
  puts "IMPOSSIBLE"
else
  before = words[0...key_index]
  after = words[key_index + 1..-1] || []

  d1 = key_index % 10
  d2 = after.length % 10
  d3 = before.join.length % 10
  d4 = after.join.length % 10

  puts "#{d1}.#{d2}.#{d3}.#{d4}"
end