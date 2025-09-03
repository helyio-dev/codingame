<?php

while (TRUE)
{
    fscanf(STDIN, "%s", $enemy1);
    fscanf(STDIN, "%d", $dist1);
    fscanf(STDIN, "%s", $enemy2);
    fscanf(STDIN, "%d", $dist2);

    if ($dist1 < $dist2) {
        echo($enemy1 . "\n");
    } else {
        echo($enemy2 . "\n");
    }
}
?>
