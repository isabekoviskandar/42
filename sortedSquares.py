def sortedSquares(nums: list):
    sorted_nums = []
    length = len(nums)
    for i in range(length):
        sorted_nums.append(nums[i] * nums[i])
    sorted_nums.sort()
    return sorted_nums


def sortedSquares2(nums: list):
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        if left_sq > right_sq:
            result[pos] = left_sq
            left += 1
        else:
            result[pos] = right_sq
            right -= 1
        pos -= 1
    return result

import random
import timeit

big_nums = sorted(random.randint(-10000, 10000) for _ in range(1_000_000))

time1 = timeit.timeit(lambda: sortedSquares(big_nums), number=10)
time2 = timeit.timeit(lambda: sortedSquares2(big_nums), number=10)

print(f"sortedSquares:  {time1:.4f} seconds")
print(f"sortedSquares2: {time2:.4f} seconds")