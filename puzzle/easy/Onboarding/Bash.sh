# game loop
while true; do
    read -r enemy1
    read -r dist1
    read -r enemy2
    read -r dist2

    if (( dist1 < dist2 )); then
        echo "$enemy1"
    else
        echo "$enemy2"
    fi
done
