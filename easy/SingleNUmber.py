from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return nums[-1]

            if nums[i] != nums[i + 1]:
                print(nums[i + 1])
                print(nums[i])
                return nums[i]
            i += 2


sol = Solution()
s = [3, 6, 1, 1, 6, 2, 2, 7, 7]
print(sol.singleNumber(s))
