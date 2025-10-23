use std::io::{self, Read};

fn beats(a: char, b: char) -> bool {
    matches!(
        (a, b),
        ('C', 'P') | ('C', 'L') |
        ('P', 'R') | ('P', 'S') |
        ('R', 'C') | ('R', 'L') |
        ('L', 'S') | ('L', 'P') |
        ('S', 'C') | ('S', 'R')
    )
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();

    let n: usize = it.next().unwrap().parse().unwrap();
    let mut num = Vec::with_capacity(n);
    let mut sign = Vec::with_capacity(n);
    let mut opp: Vec<Vec<i32>> = vec![Vec::new(); n];

    for _ in 0..n {
        let id: i32 = it.next().unwrap().parse().unwrap();
        let s: char = it.next().unwrap().chars().next().unwrap();
        num.push(id);
        sign.push(s);
    }

    let mut idx: Vec<usize> = (0..n).collect();
    let mut round = n;
    while round > 1 {
        let mut next = Vec::with_capacity(round / 2);
        for i in (0..round).step_by(2) {
            let i1 = idx[i];
            let i2 = idx[i + 1];
            let (w, l) = if beats(sign[i1], sign[i2]) {
                (i1, i2)
            } else if beats(sign[i2], sign[i1]) {
                (i2, i1)
            } else if num[i1] < num[i2] {
                (i1, i2)
            } else {
                (i2, i1)
            };
            opp[w].push(num[l]);
            next.push(w);
        }
        idx = next;
        round /= 2;
    }

    let winner = idx[0];
    println!("{}", num[winner]);
    let res: Vec<String> = opp[winner].iter().map(|x| x.to_string()).collect();
    println!("{}", res.join(" "));
}
