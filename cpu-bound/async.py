import asyncio

import time


async def cpu_bound(num):
    return sum(i*i for i in range(num))


async def find_sums(nums):
    tasks = []
    for number in nums:
        tasks.append(cpu_bound(number))
    result = await asyncio.gather(*tasks)
    return result


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(30)]
    start_time = time.time()
    result = asyncio.run(find_sums(numbers))
    duration = time.time() - start_time
    print(f"Counted {result} in {duration} seconds")