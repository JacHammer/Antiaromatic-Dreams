# Minci
# Time elapsed: < 30min
# submission: exceeded time limit :(


class Solution:
    '''
    brute force, Time complexity = O(n^3)
    '''
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        max_len = 0
        for i in range(len(s)):
            for j in range(len(s), -1, -1):
                if self.checkPalindrome(s[i:j]):
                    if len(s[i:j]) >= max_len:
                        max_len = len(s[i:j])
                        ans = s[i:j]
        return ans

    def checkPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-1 - i]:
                return False
        return True
