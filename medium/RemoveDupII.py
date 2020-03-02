# Minci
# Time elapsed: < 10 min
# submitted 1 time


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i = 0
        while i < l - 2:
            if nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:

                l -= 1
                nums.pop(i)
            else:
                i += 1
        return l


sol = Solution()
nums = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6, 7, 7, 7, 8, 9, 9, 9, 9, 9, 9]
ans = sol.removeDuplicates(nums)
print(ans)
print(nums)
