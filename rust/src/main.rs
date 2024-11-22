use sysinfo::{System, SystemExt};
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::Instant;
use std::thread::sleep;
use std::time::Duration;

fn bubble_sort(arr: &mut Vec<i32>) {
    let n = arr.len();
    for i in 0..n {
        let mut swapped = false;
        for j in 0..n - 1 - i {
            if arr[j] > arr[j + 1] {
                arr.swap(j, j + 1);
                swapped = true;
            }
        }
        if !swapped {
            break;
        }
    }
}

fn read_numbers_from_file(file_path: &str) -> io::Result<Vec<i32>> {
    let path = Path::new(file_path);
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    let mut numbers = Vec::new();

    for line in reader.lines() {
        match line {
            Ok(num_str) => {
                if let Ok(num) = num_str.trim().parse::<i32>() {
                    numbers.push(num);
                } else {
                    eprintln!("Skipping invalid number: {}", num_str);
                }
            }
            Err(e) => eprintln!("Error reading line: {}", e),
        }
    }

    Ok(numbers)
}

fn get_memory_usage() -> f64 {
    let mut sys = System::new_all();
    sys.refresh_memory();
    sys.used_memory() as f64
}

fn main() {
    let start = Instant::now();

    let file_path = "src/arq.txt";

    // Initial memory usage
    let initial_mem_usage = get_memory_usage();
    println!("Initial memory usage: {:.2} KB", initial_mem_usage);
    
    // Introduce a small delay to ensure system has updated memory readings
    sleep(Duration::from_secs(1));

    match read_numbers_from_file(file_path) {
        Ok(mut numbers) => {
            println!("Original numbers: {:?}", numbers);
            bubble_sort(&mut numbers);
            println!("Sorted numbers: {:?}", numbers);
        }
        Err(e) => eprintln!("Error reading the file: {}", e),
    }
    // Delay again before final memory usage measurement
    sleep(Duration::from_secs(1));

    let duration = start.elapsed();
    let secs = duration.as_secs() as f64 + duration.subsec_nanos() as f64 / 1_000_000_000.0;

    // Final memory usage
    let final_mem_usage = get_memory_usage();
    println!("Time: {:.4} seconds", secs);
    let memory_used = final_mem_usage - initial_mem_usage;
    // Ignore very small differences in memory usage
    if memory_used.abs() > 50.0 {
        println!("Memory used: {:.2} KB", memory_used);
    } else {
        println!("Memory used: negligible ({:.2} KB)", memory_used);
    }

    println!("Time: {:.4} seconds", secs);
}

//Tentando lidar com flututações 