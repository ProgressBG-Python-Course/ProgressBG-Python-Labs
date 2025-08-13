import multiprocessing
import time
import math


def perform_heavy_calculation(n):
    """Perform a computationally intensive calculation."""
    print(f"Processing {n} in process {multiprocessing.current_process().name}")

    # A simple but computationally intensive task
    result = 0
    for i in range(10_000_000):
        result += n * (math.sin(i * 0.00001) * math.cos(i * 0.00002))

    return f"Input: {n}, Result: {result:.6f}"


def process_without_multiprocessing(numbers):
    """Process a list of numbers sequentially."""
    start_time = time.time()
    results = []

    for number in numbers:
        results.append(perform_heavy_calculation(number))

    end_time = time.time()
    return results, end_time - start_time


def process_with_multiprocessing(numbers, num_processes=None):
    """Process a list of numbers with multiprocessing."""
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()  # Use all available CPU cores

    start_time = time.time()

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.map(perform_heavy_calculation, numbers)

    end_time = time.time()
    return results, end_time - start_time


if __name__ == "__main__":
    # Just a list of numbers for our tasks
    test_numbers = list(range(1, 9))

    print(f"Running tests on {len(test_numbers)} tasks...")
    print("CPU Count:", multiprocessing.cpu_count())

    print("\nRunning without multiprocessing...")
    single_results, single_time = process_without_multiprocessing(test_numbers)

    print("\nRunning with multiprocessing...")
    multi_results, multi_time = process_with_multiprocessing(test_numbers)

    # Compare the results
    print("\nResults:")
    print(f"Without multiprocessing: {single_time:.2f} seconds")
    print(f"With multiprocessing: {multi_time:.2f} seconds")
    print(f"Speedup: {single_time / multi_time:.2f}x")

    # Print first result from each method to verify they're the same
    print("\nSample results (first result):")
    print(f"Sequential: {single_results[0]}")
    print(f"Multiprocessing: {multi_results[0]}")
