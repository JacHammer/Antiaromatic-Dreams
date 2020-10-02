from typing import List
import random


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] += dp[i-1]
        print(dp)
        return max(dp)


sol = Solution()
arr = [random.randint(0, 100) for _ in range(10)]
print(arr)
print(sol.lengthOfLIS(arr))
