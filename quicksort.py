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


def quicksort3(nums, start, end):
    if start < end:
        pivot_idx = partition(nums, start, end)
        quicksort3(nums, start, pivot_idx - 1)
        quicksort3(nums, pivot_idx + 1, end)
        print(nums)


def partition(nums, start, end):
    print("partitioning")
    i = start - 1
    pivot = nums[end]

    for j in range(start, end):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[end] = nums[end], nums[i+1]
    return i+1  # return index if pivot

q = [7,4,6,9,0,1,3,5]
quicksort3(q, 0, len(q)-1)
print(q)
'''

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
'''