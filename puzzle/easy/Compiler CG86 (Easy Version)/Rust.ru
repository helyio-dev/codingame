use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let e: Vec<&str> = input.split_whitespace().collect();
    let mut ops = Vec::new();
    let mut i = 0;

    if e[0] == "+" || e[0] == "-" {
        let op = if e[0] == "+" { "ADD" } else { "SUB" };
        let val: i32 = e[1].parse().unwrap();
        ops.push((op, val));
        i = 2;
    } else {
        ops.push(("ADD", e[0].parse().unwrap()));
        i = 1;
    }

    while i < e.len() {
        let op = if e[i] == "+" { "ADD" } else { "SUB" };
        let val: i32 = e[i + 1].parse().unwrap();
        ops.push((op, val));
        i += 2;
    }

    let mut counts = HashMap::new();
    for (op, val) in &ops {
        *counts.entry((op.to_string(), *val)).or_insert(0) += 1;
    }

    let mut done = HashMap::new();
    for (op, val) in &ops {
        if !done.contains_key(&(op.to_string(), *val)) {
            let c = counts[&(op.to_string(), *val)];
            if c > 1 {
                println!("REPEAT {}", c);
            }
            println!("{} cgx {}", op, val);
            done.insert((op.to_string(), *val), true);
        }
    }

    println!("EXIT");
}
