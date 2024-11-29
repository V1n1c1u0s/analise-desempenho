package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime"
	"strconv"
	"time"
	"sync"
)

// Função para obter o uso de memória
func getMemoryUsage() int64 {
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)
	return int64(memStats.Sys / 1024) // Retorna em KB
}

// Função de partição de Hoare
func partition(arr []int, low, high int) int {
	pivot := arr[low]
	i := low - 1
	j := high + 1
	for {
		i++
		for arr[i] < pivot {
			i++
		}
		j--
		for arr[j] > pivot {
			j--
		}
		if i >= j {
			return j
		}
		arr[i], arr[j] = arr[j], arr[i]
	}
}

// Função de QuickSort paralelo
func quickSortParallel(arr []int, low, high int, wg *sync.WaitGroup) {
	defer wg.Done()

	if low < high {
		pi := partition(arr, low, high)

		// Dividir a tarefa entre duas Goroutines
		wg.Add(2) // Adicionar duas Goroutines para espera
		go quickSortParallel(arr, low, pi, wg)
		go quickSortParallel(arr, pi+1, high, wg)
	}
}

func main() {
	// Medir o tempo de execução
	start := time.Now()

	// Abrir o arquivo de entrada
	file, err := os.Open("arq.txt")
	if err != nil {
		fmt.Println("Erro ao abrir o arquivo:", err)
		return
	}
	defer file.Close()

	// Ler os números do arquivo
	var arr []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())
		if err != nil {
			fmt.Println("Erro ao ler o número:", err)
			return
		}
		arr = append(arr, num)
	}

	// Usar um WaitGroup para gerenciar as Goroutines
	var wg sync.WaitGroup
	wg.Add(1) // Inicializa o WaitGroup com 1 Goroutine principal

	// Executar o QuickSort paralelo
	quickSortParallel(arr, 0, len(arr)-1, &wg)

	// Esperar todas as Goroutines terminarem
	wg.Wait()

	// Salvar o resultado no arquivo de saída
	outputFile, err := os.Create("arq-saida.txt")
	if err != nil {
		fmt.Println("Erro ao abrir o arquivo de saída:", err)
		return
	}
	defer outputFile.Close()

	for _, num := range arr {
		_, err := fmt.Fprintln(outputFile, num)
		if err != nil {
			fmt.Println("Erro ao escrever no arquivo de saída:", err)
			return
		}
	}

	// Medir o tempo de execução
	duration := time.Since(start)
	fmt.Printf("Tempo de execução: %v segundos\n", duration.Seconds())

	// Obter o uso de memória
	finalMemory := getMemoryUsage()
	fmt.Printf("Uso de memória final: %d KB\n", finalMemory)
}
