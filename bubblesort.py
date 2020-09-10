def bubblesort(nums):
    if len(nums) >= 2:
        nums_sorted = False
        while not nums_sorted:
            has_swap = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    has_swap = True
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            nums_sorted = not has_swap


arr = [4, 5]
bubblesort(arr)
print(arr)
