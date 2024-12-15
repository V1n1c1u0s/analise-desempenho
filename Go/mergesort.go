package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime"
	"time"
	"strconv"
	"log"
)

func merge(arr []int, left, mid, right int) {
	n1 := mid - left + 1
	n2 := right - mid
	L := make([]int, n1)
	R := make([]int, n2)
	copy(L, arr[left:mid+1])
	copy(R, arr[mid+1:right+1])
	i, j, k := 0, 0, left
	for i < n1 && j < n2 {
		if L[i] <= R[j] {
			arr[k] = L[i]
			i++
		} else {
			arr[k] = R[j]
			j++
		}
		k++
	}
	for i < n1 {
		arr[k] = L[i]
		i++
		k++
	}
	for j < n2 {
		arr[k] = R[j]
		j++
		k++
	}
}

func mergeSort(arr []int, left, right int) {
	if left < right {
		mid := left + (right-left)/2
		mergeSort(arr, left, mid)
		mergeSort(arr, mid+1, right)
		merge(arr, left, mid, right)
	}
}

func readNumbersFromFile(filePath string) ([]int, error) {
	var numbers []int
	file, err := os.Open(filePath)
	if err != nil {	return nil, err }
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if num, err := strconv.Atoi(line); err == nil {	numbers = append(numbers, num); }
	}
	if err := scanner.Err(); err != nil { return nil, err }
	return numbers, nil
}

func getMemoryUsage() uint64 {
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)
	return memStats.Alloc / 1024 // Retorna em KB
}

func getPeakMemoryUsage() uint64 {
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)
	return memStats.TotalAlloc / 1024 // Retorna em KB
}

func main() {
	filePath := "arq-desafio.txt"
	initialMemory := getMemoryUsage()
	fmt.Printf("Mem inicial: %d KB\n", initialMemory)

	startTime := time.Now()

	numbers, err := readNumbersFromFile(filePath)
	if err != nil {	log.Fatal("Erro ao ler arq.txt: ", err) }

	afterArrayGenerationMemory := getMemoryUsage()
	fmt.Printf("Mem usada dps de gerar array: %d KB\n", afterArrayGenerationMemory)

	mergeSort(numbers, 0, len(numbers)-1)

	afterSortingMemory := getMemoryUsage()
	fmt.Printf("Mem usada dps de ord: %d KB\n", afterSortingMemory)

	outFile, err := os.Create("arq-saida.txt")
	if err != nil {	log.Fatal("Error ao criar arq-saida.txt: ", err) }
	defer outFile.Close()

	for _, item := range numbers {
		_, err := fmt.Fprintf(outFile, "%d\n", item)
		if err != nil { log.Fatal("Erro ao escrever arq-saida.txt:", err) }
	}

	executionTime := time.Since(startTime).Seconds()
	peakMemory := getPeakMemoryUsage()
	fmt.Printf("Pico de mem usada: %d KB\n", peakMemory)
	fmt.Printf("Tempo de Exec: %.4f seconds\n", executionTime)
}
