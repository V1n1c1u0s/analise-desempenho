#!/bin/bash

arqs=("bubblesort" "quicksort" "mergesort")

langs=("c" "php" "go")

caminho=("C/atv3/" "../../PHP" "../Go" "../")

rodar(){
    echo -e "$2" >> ${arqs[0]}.txt
    for i in {1..10}
    do
        echo -e "$1" >> ${arqs[0]}.txt
    done
}

for i in $arqs
do
    cd $caminho[0]
    rodar "$(./${arqs[i]} | grep -oE '[tempo|memória|+-]?[0-9]*\.[0-9]+|[+-]?[0-9]+')" "C"
    cd $caminho[1]
    rodar "$(php ${arqs[i]}'.php' | grep -oE '[peak|execution|+-]?[0-9]*\.[0-9]+|[+-]?[0-9]+')" "PHP"
    cd $caminho[2]
    rodar "$(go run ${arqs[i]}'.go' | grep -oE '[peak|execution|+-]?[0-9]*\.[0-9]+|[+-]?[0-9]+')" "Go"
    cd $caminho[3]
done

