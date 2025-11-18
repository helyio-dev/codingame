<?php

function sumDigits($n) {
    return array_sum(str_split((string)$n));
}

$r = intval(trim(fgets(STDIN)));
$c = intval(trim(fgets(STDIN)));
$t = intval(trim(fgets(STDIN)));

$visited = array_fill(0, $r, array_fill(0, $c, false));
$queue = [];
$count = 0;

if (sumDigits(0) + sumDigits(0) <= $t) {
    $queue[] = [0, 0];
    $visited[0][0] = true;
    $count = 1;
}

$directions = [[0, 1], [1, 0], [0, -1], [-1, 0]];

while (!empty($queue)) {
    list($x, $y) = array_shift($queue);
    
    foreach ($directions as $dir) {
        list($dx, $dy) = $dir;
        $nx = $x + $dx;
        $ny = $y + $dy;
        
        if ($nx >= 0 && $nx < $r && $ny >= 0 && $ny < $c && !$visited[$nx][$ny]) {
            if (sumDigits($nx) + sumDigits($ny) <= $t) {
                $visited[$nx][$ny] = true;
                $queue[] = [$nx, $ny];
                $count++;
            }
        }
    }
}

echo $count . "\n";

?>