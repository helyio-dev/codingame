sum_digits() {
    local n=$1
    local sum=0
    while [ $n -gt 0 ]; do
        sum=$((sum + n % 10))
        n=$((n / 10))
    done
    echo $sum
}

read R
read C
read T

S0=$(sum_digits 0)
if [ $S0 -gt $T ]; then
    echo 0
    exit 0
fi

declare -A visited
declare -a queue
queue[0]="0,0"
visited["0,0"]=1
count=1
head=0

dx=(1 -1 0 0)
dy=(0 0 1 -1)

while [ $head -lt ${#queue[@]} ]; do
    current_rc=${queue[head]}
    head=$((head + 1))

    r=$(echo "$current_rc" | cut -d',' -f1)
    c=$(echo "$current_rc" | cut -d',' -f2)

    for i in 0 1 2 3; do
        nx=$((r + dx[i]))
        ny=$((c + dy[i]))
        
        if [ $nx -ge 0 ] && [ $nx -lt $R ] && [ $ny -ge 0 ] && [ $ny -lt $C ]; then
            
            key="${nx},${ny}"
            
            if [ -z "${visited[$key]}" ]; then
                
                Sx=$(sum_digits $nx)
                Sy=$(sum_digits $ny)
                Sum_S=$((Sx + Sy))
                
                if [ $Sum_S -le $T ]; then
                    queue+=("$key")
                    visited[$key]=1
                    count=$((count + 1))
                fi
            fi
        fi
    done
done

echo $count