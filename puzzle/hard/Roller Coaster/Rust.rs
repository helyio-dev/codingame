use std::io::{self, BufRead};
use std::collections::HashMap;

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let lcn: Vec<u64> = lines
        .next()
        .unwrap()
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let (l, c, n) = (lcn[0], lcn[1], lcn[2]);
    let mut groups = Vec::with_capacity(n as usize);
    for _ in 0..n {
        groups.push(lines.next().unwrap().unwrap().trim().parse::<u64>().unwrap());
    }

    let mut next_index = vec![0usize; n as usize];
    let mut gain = vec![0u64; n as usize];

    for i in 0..n as usize {
        let mut total = 0;
        let mut count = 0;
        let mut j = i;
        while count < n && total + groups[j] <= l {
            total += groups[j];
            j = (j + 1) % (n as usize);
            count += 1;
        }
        next_index[i] = j;
        gain[i] = total;
    }

    let mut total_gain: u128 = 0;
    let mut cache = HashMap::new();
    let mut idx = 0usize;
    let mut ride = 0u64;

    while ride < c {
        if let Some((prev_ride, prev_gain)) = cache.get(&idx) {
            let cycle_len = ride - prev_ride;
            let cycle_gain = total_gain - prev_gain;
            if cycle_len > 0 {
                let remaining = c - ride;
                let cycles = remaining / cycle_len;
                total_gain += cycle_gain * (cycles as u128);
                ride += cycles * cycle_len;
                if ride >= c { break; }
            }
        } else {
            cache.insert(idx, (ride, total_gain));
        }
        total_gain += gain[idx] as u128;
        idx = next_index[idx];
        ride += 1;
    }

    println!("{}", total_gain);
}
