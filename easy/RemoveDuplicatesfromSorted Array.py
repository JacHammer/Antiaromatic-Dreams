from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums) - 1):
            if (nums[i] != nums[i + 1]):
                nums[x] = nums[i + 1]
                x += 1
        return (x)


nums = [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 3, 4]
sol = Solution()
print(sol.removeDuplicates(nums))
