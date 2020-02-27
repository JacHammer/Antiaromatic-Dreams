from typing import List


# 22 min
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        l = len(nums) // 2
        d = dict()
        selected_one = None
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        for key in d:
            if d[key] > l:
                return key
        return None


sol = Solution()
print(sol.majorityElement([2, 3, 3, 3, 3, 4, 5, 6]))
