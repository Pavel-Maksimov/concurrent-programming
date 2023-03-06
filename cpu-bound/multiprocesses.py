import multiprocessing
import time


def cpu_bound(num):
    return sum(i*i for i in range(num))


def find_sums(nums):
    with multiprocessing.Pool() as pool:
        result = pool.map(cpu_bound, nums)
    return result


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(30)]
    start_time = time.time()
    result = find_sums(numbers)
    duration = time.time() - start_time
    print(f"Counted {result} in {duration} seconds")