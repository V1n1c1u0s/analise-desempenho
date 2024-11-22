fn bubble_sort<T: Ord>(arr: &mut [T]) {
    let n = arr.len();
    
    // Outer loop to go over the array multiple times
    for i in 0..n {
        // Flag to check if any swap is made
        let mut swapped = false;

        // Inner loop to perform the comparison and swap
        for j in 1..n-i {
            if arr[j-1] > arr[j] {
                // Swap elements
                arr.swap(j-1, j);
                swapped = true;
            }
        }

        // If no swaps were made, the array is sorted
        if !swapped {
            break;
        }
    }
}

fn main() {
    let mut numbers = [64, 34, 25, 12, 22, 11, 90];
    
    println!("Before sorting: {:?}", numbers);
    
    bubble_sort(&mut numbers);
    
    println!("After sorting: {:?}", numbers);
}
