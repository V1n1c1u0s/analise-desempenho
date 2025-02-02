<?php
if ($argc != 3) {
    echo "Usage: php heapsort.php <input_file> <output_file>\n";
    exit(1);
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

// Function to build a max heap
function heapify(array &$arr, $n, $i) {
    $largest = $i;
    $left = 2 * $i + 1;
    $right = 2 * $i + 2;

    // Check if left child exists and is larger than the root
    if ($left < $n && $arr[$left] > $arr[$largest]) {
        $largest = $left;
    }

    // Check if right child exists and is larger than the largest so far
    if ($right < $n && $arr[$right] > $arr[$largest]) {
        $largest = $right;
    }

    // If largest is not root, swap and continue heapifying
    if ($largest != $i) {
        // Swap the elements
        list($arr[$i], $arr[$largest]) = array($arr[$largest], $arr[$i]);

        // Recursively heapify the affected subtree
        heapify($arr, $n, $largest);
    }
}

function heapSort(array &$arr) {
    $n = count($arr);

    // Build a max heap from the bottom-up
    for ($i = floor($n / 2) - 1; $i >= 0; $i--) {
        heapify($arr, $n, $i);
    }

    // Extract elements from the heap one by one
    for ($i = $n - 1; $i >= 1; $i--) {
        // Swap the root (max element) with the last element
        list($arr[0], $arr[$i]) = array($arr[$i], $arr[0]);

        // Heapify the root to restore the heap property
        heapify($arr, $i, 0);
    }
}

function getPeakMemoryUsage() {
    return memory_get_peak_usage(true) / 1024; // KB
}

$filePath = $argv[1];

$startTime = microtime(true);

$arr = readNumbersFromFile($filePath);

heapSort($arr);

$outFile = fopen($argv[2], "w");
foreach($arr as $item){
    fwrite($outFile, $item . PHP_EOL);
}
fclose($outFile);

$executionTime = microtime(true) - $startTime;
$peakMemory = getPeakMemoryUsage();
echo "Execution time: " . number_format($executionTime, 4) . " seconds\n";
echo "Peak memory usage: " . $peakMemory . " KB\n";
?>
