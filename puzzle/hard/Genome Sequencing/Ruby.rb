puts (1..gets.to_i).map { gets.strip }.permutation.map {|x|
    r = ''
    x.each {|x|
        [r, x].map(&:length).min.downto(0).each {|l|
            if r.chars.last(l).join == x[0...l] then
                r += x[l...x.length]
                break
            end
        } if !r.include? x
    }
    r.length
}.min