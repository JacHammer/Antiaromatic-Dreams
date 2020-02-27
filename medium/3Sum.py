from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol_set = []
        nums.sort()
        for i in range(len(nums) - 2):
            # ignore duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # if nums[i] > 0, then the sum of any two elements on its right will be greater than 0            
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    # sum = 0
                    sub_sol = [nums[i], nums[l], nums[r]]
                    sol_set.append(sub_sol)
                    # check duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return sol_set


sol = Solution()
print(sol.threeSum([0, 0, 0]))
