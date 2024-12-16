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
        echo -e "$1" >> "$2.txt"
    done
}

for i in "${arqs[@]}"
do
    # Rodando o programa C
    cd "${caminho[0]}" || { echo "Erro: diretório ${caminho[0]} não encontrado"; exit 1; }
    rodar "$(./$i | grep -oE '[+-]?[0-9]*\.[0-9]+|[+-]?[0-9]+')" "$i-cpp"

    # Rodando o programa PHP
    cd "${caminho[1]}" || { echo "Erro: diretório ${caminho[1]} não encontrado"; exit 1; }
    rodar "$(php "$i.php" | grep -oE "[+-]?[0-9]*\.[0-9]+|[+-]?[0-9]+")" "$i-php"

    # Rodando o programa Go
    cd "${caminho[2]}" || { echo "Erro: diretório ${caminho[2]} não encontrado"; exit 1; }
    rodar "$(go run "$i.go" | grep -oE "[+-]?[0-9]*\.[0-9]+|[+-]?[0-9]+")" "$i-go"

    # Voltando ao diretório base
    cd "${caminho[3]}"
done
