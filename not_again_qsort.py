def partition(nums, start, end):
    i = start - 1
    pivot = nums[end]
    for j in range(start, end):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1


def qsort(nums, start, end):
    if start < end:
        pivot_idx = partition(nums, start, end)
        qsort(nums, start, pivot_idx - 1)
        qsort(nums, pivot_idx + 1, end)


q = [635, 253, 63, 74, 859, 657, 647, 54, 5, 3647, 5686, 9780, 96857, 6453, 4, 324, 53564, 65]
qsort(q, 0, len(q)-1)
print(q)
