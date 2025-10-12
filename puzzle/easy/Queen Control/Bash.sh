read QUEEN_COLOR_STR

if [[ "$QUEEN_COLOR_STR" == "white" ]]; then
    QUEEN_COLOR="w"
    OPPONENT_COLOR="b"
else
    QUEEN_COLOR="b"
    OPPONENT_COLOR="w"
fi

BOARD=()
for i in {0..7}; do
    read LINE
    BOARD+=("$LINE")
done

QR=-1
QC=-1
for R in {0..7}; do
    LINE="${BOARD[R]}"
    for C in {0..7}; do
        if [[ "${LINE:C:1}" == "Q" ]]; then
            QR=$R
            QC=$C
            break
        fi
    done
    if [ $QR -ne -1 ]; then
        break
    fi
done

CONTROLLED_SQUARES=0
DIRECTIONS=(-1 0 1 0 0 -1 0 1 -1 -1 -1 1 1 -1 1 1)

for i in {0..7}; do
    DR=${DIRECTIONS[2*i]}
    DC=${DIRECTIONS[2*i+1]}
    
    R=$QR
    C=$QC
    
    while true; do
        R=$((R + DR))
        C=$((C + DC))
        
        if ! ( [ $R -ge 0 ] && [ $R -le 7 ] && [ $C -ge 0 ] && [ $C -le 7 ] ); then
            break
        fi
        
        PIECE="${BOARD[R]:C:1}"
        
        if [[ "$PIECE" == "." ]]; then
            CONTROLLED_SQUARES=$((CONTROLLED_SQUARES + 1))
            continue
        fi

        if [[ "$PIECE" == "$QUEEN_COLOR" || "$PIECE" == "Q" ]]; then
            break
        fi
        
        if [[ "$PIECE" == "$OPPONENT_COLOR" ]]; then
            CONTROLLED_SQUARES=$((CONTROLLED_SQUARES + 1))
            break
        fi

    done
done

echo "$CONTROLLED_SQUARES"