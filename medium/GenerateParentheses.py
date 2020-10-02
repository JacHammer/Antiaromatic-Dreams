from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        if n == 0:
            return ans

        return ans


sol = Solution()
n_parentheses = 3
answer = sol.generateParenthesis(n_parentheses)
print(answer)
