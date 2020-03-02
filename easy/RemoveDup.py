from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n_dup = 0
        l = len(nums)
        i = 0
        while i < l - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
                # i += 1
                l -= 1
            else:
                i += 1
        return l


sol = Solution()
nums = [1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9]
ans = sol.removeDuplicates(nums)
print(ans)
print(nums)