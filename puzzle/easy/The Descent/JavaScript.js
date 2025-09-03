while (true) {
    let maxH = -1;
    let mountainToFire = 0;

    for (let i = 0; i < 8; i++) {
        const mountainH = parseInt(readline());
        if (mountainH > maxH) {
            maxH = mountainH;
            mountainToFire = i;
        }
    }
    console.log(mountainToFire);
}
