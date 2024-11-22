<?php

ini_set('memory_limit', '512M');  // This ensures PHP can use more memory

function bubbleSort(array &$arr) {
    $n = count($arr);
    for ($i = 0; $i < $n; $i++) {
        $swapped = false;
        for ($j = 0; $j < $n - 1 - $i; $j++) {
            if ($arr[$j] > $arr[$j + 1]) {
                // Swap the elements
                $temp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $temp;
                $swapped = true;
            }
        }
        // If no elements were swapped, the array is already sorted
        if (!$swapped) {
            break;
        }
    }
}

function readNumbersFromFile($filePath) {
    $numbers = [];
    $file = fopen($filePath, "r");
    if ($file) {
        while (($line = fgets($file)) !== false) {
            $line = trim($line);
            // Try to parse each line as an integer
            if (is_numeric($line)) {
                $numbers[] = (int)$line;
            } else {
                echo "Skipping invalid number: $line\n";
            }
        }
        fclose($file);
    } else {
        echo "Error opening the file.\n";
    }

    return $numbers;
}

function getMemoryUsage() {
    // Returns the memory usage in kilobytes
    return memory_get_usage(true) / 1024; // KB
}

function getPeakMemoryUsage() {
    // Returns the peak memory usage in kilobytes
    return memory_get_peak_usage(true) / 1024; // KB
}

// Set a higher memory limit if necessary
ini_set('memory_limit', '512M');  // Increase memory limit to 512MB

$filePath = "arq.txt";  // Replace with your file path

// Measure initial memory usage
$initialMemory = getMemoryUsage();
echo "Initial memory usage: " . $initialMemory . " KB\n";

// Start the timer
$startTime = microtime(true);

// Generate a large array of numbers (30,000 numbers)
$numbers = readNumbersFromFile($filePath);

// Track memory after array generation
$afterArrayGenerationMemory = getMemoryUsage();
echo "Memory usage after generating array: " . $afterArrayGenerationMemory . " KB\n";

// Perform bubble sort
bubbleSort($numbers);

// Track memory after sorting
$afterSortingMemory = getMemoryUsage();
echo "Memory usage after sorting: " . $afterSortingMemory . " KB\n";

// Measure execution time
$executionTime = microtime(true) - $startTime;

// Measure peak memory usage
$peakMemory = getPeakMemoryUsage();
echo "Peak memory usage: " . $peakMemory . " KB\n";

// Display results
echo "Sorted numbers (first 10): " . implode(", ", array_slice($numbers, 0, 10)) . "...\n";
echo "Execution time: " . number_format($executionTime, 4) . " seconds\n";
