package main

import (
	"bufio"
	"fmt"
	"os"
	"runtime"
	"strconv"
	"time"
	"log"
)

// Bubble Sort implementation
func bubbleSort(arr []int) {
	n := len(arr)
	for i := 0; i < n; i++ {
		swapped := false
		for j := 0; j < n-1-i; j++ {
			if arr[j] > arr[j+1] {
				// Swap elements
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}
}

// Get the current memory usage
func getMemoryUsage() uint64 {
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)
	return memStats.Sys / 1024 // Return memory in KB
}

// Read numbers from a file
func readNumbersFromFile(filePath string) ([]int, error) {
	var numbers []int
	file, err := os.Open(filePath)
	if err != nil {
		return nil, err
	}
	defer file.Close()  // Ensures file is closed after reading

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		numStr := scanner.Text()
		num, err := strconv.Atoi(numStr)
		if err != nil {
			return nil, fmt.Errorf("invalid number in file: %s", numStr)
		}
		numbers = append(numbers, num)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return numbers, nil
}


func main() {
	filePath := "arq-desafio.txt"

	// Measure initial memory usage
	initialMemory := getMemoryUsage()
	fmt.Printf("Initial memory usage: %d KB\n", initialMemory)

	// Start timer
	startTime := time.Now()

	// Read numbers from file
	numbers, err := readNumbersFromFile(filePath)
	if err != nil {
		fmt.Printf("Error reading the file: %v\n", err)
		return
	}

	// Memory usage after reading file
	afterFileReadMemory := getMemoryUsage()
	fmt.Printf("Memory usage after reading file: %d KB\n", afterFileReadMemory)

	// Perform bubble sort
	bubbleSort(numbers)
	//fmt.Printf("Sorted array: %d", numbers)
	// Memory usage after sorting
	afterSortingMemory := getMemoryUsage()
	fmt.Printf("Memory usage after sorting: %d KB\n", afterSortingMemory)

	outFile, err := os.Create("arq-saida.txt")
	if err != nil {	log.Fatal("Cannot create arq-saida.txt: ", err) }
	defer outFile.Close()

	for _, item := range numbers {
		_, err := fmt.Fprintf(outFile, "%d\n", item)
		if err != nil { log.Fatal("Error writing to arq-saida.txt:", err) }
	}

	// Measure execution time
	elapsed := time.Since(startTime).Seconds()
	fmt.Printf("Execution time: %.4f seconds\n", elapsed)

	// Display peak memory usage
	fmt.Printf("Peak memory usage: %d KB\n", afterSortingMemory)
}
