translator = {
1=>"I",
4=>"IV",
5=>"V",
9=>"IX",
10=>"X",
40=>"XL",
50=>"L",
90=>"XC",
100=>"C",
400=>"CD",
500=>"D",
900=>"CM",
1000=>"M"}
values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

numbers = [] 
gets.to_i.times do
  tmp = value = gets.to_i
  roman = ""
  i = 0
  while value != 0
    if value - values[i] >= 0
      roman+=translator[values[i]]
      value -= values[i]
    else
      i+=1
    end
  end
  numbers << [roman, tmp]
end

numbers.sort!()
puts numbers.map{|num , x| x}.join " "