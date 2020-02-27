class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        for i in range(len(s)):
            if s[i] != s[-i - 1]:
                print(str(s[i]) + ' ' + str(s[-i - 1]))
                return False

        return True


sol = Solution()
my_int = 1010
print(sol.isPalindrome(my_int))
