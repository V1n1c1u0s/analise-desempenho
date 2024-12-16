#!/bin/bash
arqs=("bubblesort" "quicksort" "mergesort")
caminho=("C/atv3" "../../PHP" "../Go" "../")


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

for i in "${arqs[@]}"
do
    cd "${caminho[0]}" || { echo "Erro: diretório ${caminho[0]} não encontrado"; exit 1; }
    rodar "./$i" "$i-cpp"
    python3 ../../Graficos/main.py "$i-cpp.txt"

    cd "${caminho[1]}" || { echo "Erro: diretório ${caminho[1]} não encontrado"; exit 1; }
    rodar "php $i.php" "$i-php"
    python3 ../Graficos/main.py "$i-php.txt"

    cd "${caminho[2]}" || { echo "Erro: diretório ${caminho[2]} não encontrado"; exit 1; }
    rodar "go run $i.go" "$i-go"
    python3 ../Graficos/main.py "$i-go.txt"

    cd "${caminho[3]}"
    
done



