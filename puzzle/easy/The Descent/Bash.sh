while true; do
    max_h=-1
    mountain_to_fire=0
    for (( i=0; i<8; i++ )); do
        read -r mountain_h
        if (( mountain_h > max_h )); then
            max_h=$mountain_h
            mountain_to_fire=$i
        fi
    done
    echo "$mountain_to_fire"
done
