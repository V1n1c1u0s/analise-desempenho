<?php
    if ($argc < 2) {
        echo "Usage: php generate.php <arg1> ...\n";
        exit(1);
    }
    for ($i = 1; $i < $argc; $i++) {
        $file = fopen("$argv[$i]-num.txt","w");
        if($file) {
            for($j=0; $j < $argv[$i]; $j++) {
                $randomSeed = microtime(true)*rand();
                srand($randomSeed);
                $number = rand()%100000;
                if($j < $argv[$i]-1)
                    fwrite($file,"$number\n");
                else
                    fwrite($file,"$number");
            }
        } else {
            echo "Erro\n";
        }
        fclose($file);
    }
?>