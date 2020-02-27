class Solution:
    def isValid(self, s: str) -> bool:
        pair = {']': '[', ')': '(', '}': '{'}
        stack = []
        for c in s:
            if c not in stack:
                if c in pair.keys() and s[0] not in pair.keys() and stack != []:
                    if pair[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return stack == []


sol = Solution()
my_p = '[])'
print(sol.isValid(my_p))
