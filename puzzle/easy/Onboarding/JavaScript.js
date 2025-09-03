while (true) {
    const enemy1 = readline();
    const dist1 = parseInt(readline());
    const enemy2 = readline();
    const dist2 = parseInt(readline());

    if (dist1 < dist2) {
        console.log(enemy1);
    } else {
        console.log(enemy2);
    }
}
