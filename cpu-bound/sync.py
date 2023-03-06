import time


def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    for number in numbers:
        result = (number, cpu_bound(number))
    return result


if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(30)]

    start_time = time.time()
    result = find_sums(numbers)
    duration = time.time() - start_time
    print(f"Counted {result} in {duration} seconds")