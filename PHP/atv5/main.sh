#!/bin/bash
programas=("heapsort" "quicksort" "mergesort")
arquivos=("10000" "50000" "100000")

rodar(){
    if [ -e "$2.txt" ]; then
        echo "Arquivo "$2.txt" já existe. Removendo..."
        rm "$2.txt"
    fi
    for j in {1..10}
    do
        $1 | grep -oE '[+-]?[0-9]*\.[0-9]+|[+-]?[0-9]+' >> "$2.txt"
    done
}

for i in "${arquivos[@]}"
do
    php generate.php $i
    for j in "${programas[@]}"
    do
        rodar "php $j.php $i-num.txt $i-$j-output.txt" "time-$i-$j"
    done
done
for k in "${arquivos[@]}"
do
    for l in "${programas[@]}"
    do
        python3 main.py "time-$k-$l.txt"
    done
    python3 grap.py --number $k
done



