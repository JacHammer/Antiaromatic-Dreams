class Solution:
    def twoSum(self, nums, target):
        my_dict = {}
        for i, j in enumerate(nums):
            comp = target - j
            if comp in my_dict:
                return [my_dict[comp], i]
            else:
                my_dict[j] = i


nums = [1, 2, 10, 16]
target = 17
sol = Solution()
my_sol = sol.twoSum(nums, target)
print(my_sol)
