<?php

function merge(&$arr, $left, $mid, $right) {
    // Tamanhos dos subarrays
    $n1 = $mid - $left + 1;
    $n2 = $right - $mid;

    // Arrays temporários
    $L = array_slice($arr, $left, $n1);
    $R = array_slice($arr, $mid + 1, $n2);

    // Índices para percorrer os arrays temporários
    $i = 0;  // Índice do array L
    $j = 0;  // Índice do array R
    $k = $left; // Índice do array original

    // Mescla os arrays L e R
    while ($i < $n1 && $j < $n2) {
        if ($L[$i] <= $R[$j]) {
            $arr[$k] = $L[$i];
            $i++;
        } else {
            $arr[$k] = $R[$j];
            $j++;
        }
        $k++;
    }

    // Copia os elementos restantes de L, se houver
    while ($i < $n1) {
        $arr[$k] = $L[$i];
        $i++;
        $k++;
    }

    // Copia os elementos restantes de R, se houver
    while ($j < $n2) {
        $arr[$k] = $R[$j];
        $j++;
        $k++;
    }
}

function mergeSort(&$arr, $left, $right) {
    if ($left < $right) {
        // Encontra o ponto médio
        $mid = floor(($left + $right) / 2);

        // Ordena as duas metades
        mergeSort($arr, $left, $mid);
        mergeSort($arr, $mid + 1, $right);

        // Mescla as duas metades ordenadas
        merge($arr, $left, $mid, $right);
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
//$initialMemory = getMemoryUsage();
//echo "Initial memory usage: " . $initialMemory . " KB\n";

$startTime = microtime(true);

$numbers = readNumbersFromFile($filePath);

//$afterArrayGenerationMemory = getMemoryUsage();
//echo "Memory usage after generating array: " . $afterArrayGenerationMemory . " KB\n";

$inicio = 0;
$fim = sizeof($numbers) - 1;

mergeSort($numbers, $inicio, $fim);

//$afterSortingMemory = getMemoryUsage();
//echo "Memory usage after sorting: " . $afterSortingMemory . " KB\n";


$outFile = fopen("arq-saida.txt", "w");
foreach($numbers as $item){
    fwrite($outFile, $item . PHP_EOL);
}
fclose($outFile);

$executionTime = microtime(true) - $startTime;
$peakMemory = getPeakMemoryUsage();
echo "Execution time: " . number_format($executionTime, 4) . " seconds\n";
echo "Peak memory usage: " . $peakMemory . " KB\n";
?>
