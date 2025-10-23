def solve
    n = gets.to_i
    
    if n <= 0
        return
    end

    fib = [1, 2]
    
    loop do
        next_fib = fib[-1] + fib[-2]
        if next_fib > n
            break
        end
        fib << next_fib
    end

    representation = []
    
    fib.reverse.each do |f|
        if n >= f
            representation << f.to_s
            n -= f
        end
    end

    puts representation.join('+')
end

solve