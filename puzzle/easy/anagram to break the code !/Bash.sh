#!/bin/bash

read -r word_to_match
read -r sentence

is_anagram() {
    local w1=$(echo "${1,,}" | grep -o . | sort | tr -d '\n')
    local w2=$(echo "${2,,}" | grep -o . | sort | tr -d '\n')
    
    if [ "${1,,}" == "${2,,}" ]; then
        return 1
    fi
    
    [ "$w1" == "$w2" ]
}

clean_s=$(echo "$sentence" | tr -c 'a-zA-Z' ' ')
read -ra words <<< "$clean_s"

key_index=-1
for i in "${!words[@]}"; do
    if is_anagram "$word_to_match" "${words[$i]}"; then
        key_index=$i
        break
    fi
done

if [ "$key_index" -eq -1 ]; then
    echo "IMPOSSIBLE"
else
    d1=$((key_index % 10))
    
    after_count=$((${#words[@]} - key_index - 1))
    d2=$((after_count % 10))
    
    before_letters=0
    for ((i=0; i<key_index; i++)); do
        before_letters=$((before_letters + ${#words[$i]}))
    done
    d3=$((before_letters % 10))
    
    after_letters=0
    for ((i=key_index+1; i<${#words[@]}; i++)); do
        after_letters=$((after_letters + ${#words[$i]}))
    done
    d4=$((after_letters % 10))
    
    echo "$d1.$d2.$d3.$d4"
fi