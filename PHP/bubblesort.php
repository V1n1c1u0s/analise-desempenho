<?php

function bubbleSort(array &$arr) {
    $n = count($arr);
    for ($i = 0; $i < $n; $i++) {
        $swapped = false;
        for ($j = 0; $j < $n - 1 - $i; $j++) {
            if ($arr[$j] > $arr[$j + 1]) {
                $temp = $arr[$j];
                $arr[$j] = $arr[$j + 1];
                $arr[$j + 1] = $temp;
                $swapped = true;
            }
        }
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

$filePath = "arq-desafio.txt";
$initialMemory = getMemoryUsage();
echo "Initial memory usage: " . $initialMemory . " KB\n";

$startTime = microtime(true);

$numbers = readNumbersFromFile($filePath);

$afterArrayGenerationMemory = getMemoryUsage();
echo "Memory usage after generating array: " . $afterArrayGenerationMemory . " KB\n";

$inicio = 0;
$fim = sizeof($numbers) - 1;

bubbleSort($numbers);

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