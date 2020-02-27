from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        l = []
        start = 0
        while n > 1:
            l.append(start + 1)
            l.append(-(start + 1))
            start += 1
            n -= 2
        if n == 1:
            l.append(0)
        return l


sol = Solution()
print(sol.sumZero(5))
