# Minci
# Time elapsed: 6 min
# Submitted 1 time

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        for i in range(len(digits)):
            multiplier = 10 ** (len(digits) - i - 1)
            s += digits[i] * multiplier
        s += 1
        sum_str = str(s)
        return [str(i) for i in sum_str]


sol = Solution()
ans = sol.plusOne([9, 9, 9, 9, 9, 9])
print(ans)
