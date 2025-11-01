const m2nums = _ => readline().split(' ').map(Number);
const [xA, yA, xB, yB] = m2nums();

const gcd = (a, b) => b === 0 ? Math.abs(a) : gcd(b, a % b);
const gcd3 = (a, b, c) => gcd(gcd(a, b), c);

const normalize = ([a, b, c]) => {
    const common = gcd3(a, b, c);
    if (common === 0) return [0, 0, 0];
    a /= common;
    b /= common;
    c /= common;

    if (a < 0 || (a === 0 && b < 0)) {
        a *= -1;
        b *= -1;
        c *= -1;
    }
    return [a, b, c];
};

const V = (x, y, [a, b, c]) => a * x + b * y + c;

const n = +readline();
const eqs = new Set();
for (let i = 0; i < n; i++) {
    const rawEq = m2nums();
    const normalizedEq = normalize(rawEq);
    eqs.add(normalizedEq.join(',')); 
}

let separations = 0;
let onALine = false;

for (const eqStr of eqs) {
    const eq = eqStr.split(',').map(Number);
    
    const VA = V(xA, yA, eq);
    const VB = V(xB, yB, eq);
    
    if (VA === 0 || VB === 0) {
        onALine = true;
        break; 
    }
    
    if (VA * VB < 0) {
        separations++;
    }
}

if (onALine) {
    print('ON A LINE');
} else {
    print(separations % 2 === 0 ? 'YES' : 'NO');
}