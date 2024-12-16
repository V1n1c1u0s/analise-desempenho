<?php

function swap(&$a, &$b) {
    $temp = $a;
    $a = $b;
    $b = $temp;
}

function partition(&$arr, $low, $high) {
    $pivot = $arr[$high];
    $i = $low - 1;
    echo 'low:high'.$low.''.$high;
    for ($j = $low; $j <= $high - 1; $j++) {
        if ($arr[$j] < $pivot) {
            $i++;
            swap($arr[$i], $arr[$j]);
        }
    }
    swap($arr[$i + 1], $arr[$high]);  
    echo 'pivot: '.$pivot.'After Partition: ';
    foreach($arr as $it){
        echo $it.',';
    }
    echo 'pivot: '.$i+1 . PHP_EOL;
    return $i + 1;
}

function quickSort(array &$arr, int $low, int $high) {
    if ($low < $high) {
        $pi = partition($arr, $low, $high);
        quickSort($arr, $low, $pi - 1);
        quickSort($arr, $pi + 1, $high);
    }
}

function getMemoryUsage() {
    return memory_get_usage(true) / 1024; // KB
}

function getPeakMemoryUsage() {
    return memory_get_peak_usage(true) / 1024; // KB
}

$initialMemory = getMemoryUsage();
echo "Initial memory usage: " . $initialMemory . " KB\n";

$startTime = microtime(true);

$numbers = [10,6,9,7,2,5,1];

$afterArrayGenerationMemory = getMemoryUsage();
echo "Memory usage after generating array: " . $afterArrayGenerationMemory . " KB\n";

$inicio = 0;
$fim = sizeof($numbers) - 1;

quickSort($numbers, $inicio, $fim);

$afterSortingMemory = getMemoryUsage();
echo "Memory usage after sorting: " . $afterSortingMemory . " KB\n";

foreach($numbers as $item){
    echo $item . PHP_EOL;
}

$executionTime = microtime(true) - $startTime;
$peakMemory = getPeakMemoryUsage();
echo "Peak memory usage: " . $peakMemory . " KB\n";
echo "Execution time: " . number_format($executionTime, 4) . " seconds\n";