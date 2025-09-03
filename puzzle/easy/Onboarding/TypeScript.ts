while (true) {
    const enemy1: string = readline();
    const dist1: number = parseInt(readline());
    const enemy2: string = readline();
    const dist2: number = parseInt(readline());

    if (dist1 < dist2) {
        console.log(enemy1);
    } else {
        console.log(enemy2);
    }
}
