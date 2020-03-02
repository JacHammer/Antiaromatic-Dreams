# recap quicksort

import random
import time


def quicksort(nums):
    # base case
    if len(nums) <= 1:
        return nums
    else:
        #pivot_idx = random.randint(0, len(nums)-1)
        pivot_idx = len(nums) // 2
        pivot = nums[pivot_idx]
        left = nums[0:pivot_idx]
        right = nums[pivot_idx + 1:len(nums)]
        l = []
        r = []
        for i in left + right:
            if i < pivot:
                l.append(i)
            elif i >= pivot:
                r.append(i)

        return quicksort(l) + [pivot] + quicksort(r)


nums = [random.randint(0,1000000) for i in range(10000000)]
start = time.time()
ans = quicksort(nums)
t = time.time()-start
print(t)
