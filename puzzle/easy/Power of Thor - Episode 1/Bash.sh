read lightX lightY x y

while true; do

    read remainingTurns
    move=""

    if ((y > lightY)); then
      move+="N"
      let "y--"
    elif ((y < lightY)); then
      move+="S"
      let "y++"
    fi

    if ((x > lightX)); then
      move+="W"
      let "x--"
    elif ((x < lightX)); then
      move+="E"
      let "x++"
    fi

    echo $move
done