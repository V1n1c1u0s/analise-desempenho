<?php

function swap(&$a, &$b) {
    $temp = $a;
    $a = $b;
    $b = $temp;
}

function partition(&$arr, $low, $high) {
    $pivot = $arr[$high];
    $i = $low - 1;
    for ($j = $low; $j <= $high - 1; $j++) {
        if ($arr[$j] < $pivot) {
            $i++;
            swap($arr[$i], $arr[$j]);
        }
    }
    swap($arr[$i + 1], $arr[$high]);  
    return $i + 1;
}

function quickSort(array &$arr, int $low, int $high) {
    if ($low < $high) {
        $pi = partition($arr, $low, $high);
        quickSort($arr, $low, $pi - 1);
        quickSort($arr, $pi + 1, $high);
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
    return memory_get_usage(true) / 1024; // KB
}

function getPeakMemoryUsage() {
    return memory_get_peak_usage(true) / 1024; // KB
}

$filePath = "arq.txt";
$initialMemory = getMemoryUsage();
echo "Initial memory usage: " . $initialMemory . " KB\n";

$startTime = microtime(true);

$numbers = readNumbersFromFile($filePath);

$afterArrayGenerationMemory = getMemoryUsage();
echo "Memory usage after generating array: " . $afterArrayGenerationMemory . " KB\n";

$inicio = 0;
$fim = sizeof($numbers) - 1;

quickSort($numbers, $inicio, $fim);

$afterSortingMemory = getMemoryUsage();
echo "Memory usage after sorting: " . $afterSortingMemory . " KB\n";


$outFile = fopen("arq-saida.txt", "w");
foreach($numbers as $item){
    fwrite($outFile, $item . PHP_EOL);
}
fclose($outFile);

$executionTime = microtime(true) - $startTime;
$peakMemory = getPeakMemoryUsage();
echo "Peak memory usage: " . $peakMemory . " KB\n";
echo "Execution time: " . number_format($executionTime, 4) . " seconds\n";