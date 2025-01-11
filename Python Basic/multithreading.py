from multiprocessing import Pool, cpu_count
import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    """Find all primes in a specific range."""
    primes = [n for n in range(start, end) if is_prime(n)]
    return primes

def calculate_primes(limit):
    """Calculate prime numbers up to the given limit using multiprocessing."""
    # Determine the number of processes to use
    num_processes = cpu_count()
    print(f"Using {num_processes} processes...")

    # Divide the range into chunks for each process
    chunk_size = limit // num_processes
    ranges = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes)]
    ranges[-1] = (ranges[-1][0], limit + 1)  # Ensure the last range includes the limit

    # Use a Pool to process the chunks in parallel
    with Pool(processes=num_processes) as pool:
        results = pool.starmap(find_primes_in_range, ranges)

    # Combine all results into a single list
    primes = [prime for sublist in results for prime in sublist]
    return primes

if __name__ == "__main__":
    # Input the upper limit for prime calculation
    limit = int(input("Enter the upper limit to find prime numbers: "))

    # Calculate prime numbers
    primes = calculate_primes(limit)

    # Display the results
    print(f"Prime numbers up to {limit}:")
    print(primes)
