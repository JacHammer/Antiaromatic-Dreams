# Minci
# time elapsed: 54 min
# submitted 1 time

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shift = k % len(nums)
        for i in range(len(nums) - shift):
            temp = nums[0]
            nums.pop(0)
            nums.append(temp)


sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
sol.rotate(nums, 3)
print(nums)
