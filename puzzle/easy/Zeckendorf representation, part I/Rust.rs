use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    if io::stdin().read_to_string(&mut input).is_err() {
        return;
    }

    let n: u64 = match input.trim().parse() {
        Ok(val) => val,
        Err(_) => return,
    };

    if n <= 0 {
        return;
    }

    let mut fib: Vec<u64> = Vec::new();
    if n >= 1 {
        fib.push(1);
    }
    if n >= 2 {
        fib.push(2);
    }

    loop {
        if fib.len() < 2 {
            break;
        }
        let next_fib = fib[fib.len() - 1] + fib[fib.len() - 2];
        if next_fib > n {
            break;
        }
        fib.push(next_fib);
    }

    let mut remaining_n = n;
    let mut representation: Vec<String> = Vec::new();
    
    for f in fib.iter().rev() {
        if remaining_n >= *f {
            representation.push(f.to_string());
            remaining_n -= *f;
        }
    }

    println!("{}", representation.join("+"));
}