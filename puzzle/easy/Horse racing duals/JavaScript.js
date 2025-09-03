const N = +readline();
const powers = [];

for (let i = 0; i < N; i++) {
    powers.push(+readline());
}

powers.sort((a, b) => a - b);

let minDiff = Infinity;
for (let i = 1; i < N; i++) {
    const diff = powers[i] - powers[i - 1];
    if (diff < minDiff) {
        minDiff = diff;
    }
}

print(minDiff);
