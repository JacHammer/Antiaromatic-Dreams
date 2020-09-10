import random


def qsort(arr):
    # array with 0 or 1 element is automatically sorted
    if len(arr) <= 1:
        return arr

    # the case where the length of array is larger than 1
    else:
        # pick a pivot, here the median is chosen
        pivot_idx = len(arr) // 2

        # left side of the pivot
        left_after_arrangement = []

        # right side of the pivot
        right_after_arrangement = []

        # iterate through the array
        for idx in range(len(arr)):

            # the pivot should be ignored when iterating through the array
            if idx == pivot_idx:
                continue

            # anything that is bigger than pivot is added to right side
            if arr[idx] > arr[pivot_idx]:
                right_after_arrangement.append(arr[idx])

            # anything that is smaller than/ equal to pivot is added to left side
            else:
                left_after_arrangement.append(arr[idx])

        #  sort left part and right part, dont forget pivot
        return qsort(left_after_arrangement) + [arr[pivot_idx]] + qsort(right_after_arrangement)


array = [random.randint(0, 1000) for _ in range(10)]
print(qsort(array))
