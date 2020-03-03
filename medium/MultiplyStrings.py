# Minci
# Time elapsed: 19 min
# submitted 2 times


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = self.stoi(num1) * self.stoi(num2)
        return str(product)

    # hey let's reinvent wheels again!
    def stoi(self, string):
        # assume string is a representation of non-negative int
        # s is the current sum
        s = 0
        for i in range(len(string)):
            multiplier = 10 ** (len(string) - i - 1)
            s += int(string[i]) * multiplier
        return s


sol = Solution()
ans = sol.multiply('123', '456')
print(ans)