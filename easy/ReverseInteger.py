class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = abs(x)
        elif x > 0:
            sign = 1
        elif x == 0:
            return 0
        s = str(x)
        s = s[::-1]
        i = int(s)
        if i < pow(2, 31):
            return i * sign
        else:
            return 0


sol = Solution()
my_int = sol.reverse(-0
9809)
print(my_int)
