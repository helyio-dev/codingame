const firstInitInput = +readline();
const secondInitInput = +readline();
const thirdInitInput = +readline();

while(1) {
    const [a, b, c, d] = [readline(), readline(), readline(), readline()];

    const pairs = new Array(thirdInitInput);
    for(let i = 0; i < thirdInitInput; ++i) {
        const [x,y] = readline().split(' ').map(Number);
        pairs[i] = {x, y};
    }

    console.log(
        firstInitInput > 50 ? 'C' :
        a === 'Z' && pairs[0]?.y > 100 ? 'D' : 
        b === 'M' ? 'B' : 
        pairs[1]?.x < pairs[0]?.x ? 'A' : 'E'
    );
}
