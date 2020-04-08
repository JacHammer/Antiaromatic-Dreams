# recap quicksort

import random
import time


def quicksort1(nums):
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

        return quicksort1(l) + [pivot] + quicksort1(r)



def quicksort2(nums):
    # base case
    if len(nums) <= 1:
        return nums
    else:
        #pivot_idx = random.randint(0, len(nums)-1)
        pivot_idx = len(nums) // 2
        pivot = nums[pivot_idx]

        l = []
        r = []
        for number in nums[0:pivot_idx] + nums[pivot_idx + 1:len(nums)]:
            if number < pivot:
                l.append(number)
            elif number >= pivot:
                r.append(number)

        return quicksort2(l) + [pivot] + quicksort2(r)


time_sum1 = 0
for i in range(10):
    nums = [random.randint(0,100000) for i in range(100000)]
    start = time.time()
    ans = quicksort1(nums)
    t = time.time()-start
    time_sum1 += t

print(time_sum1 / 10)


time_sum2 = 0
for i in range(10):
    nums = [random.randint(0,100000) for i in range(100000)]
    start = time.time()
    ans = quicksort2(nums)
    t = time.time()-start
    time_sum2 += t

print(time_sum2 / 10)

time_sum3 = 0
for i in range(10):
    nums = [random.randint(0,100000) for i in range(100000)]
    start = time.time()
    ans = nums.sort()
    t = time.time()-start
    time_sum3 += t

print(time_sum3 / 10)