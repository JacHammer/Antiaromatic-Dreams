class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        perm = ''
        perm_len = 0
        temp = 0
        for index in range(len(s)):
            if temp >= len(s[index:]) and temp > perm_len:
                return temp
            curr = ''
            curr_len = 0
            d = {}
            for i, c in enumerate(s[index:]):

                if c not in d:
                    d[c] = i
                    curr += c
                    temp = len(curr)
                    print(curr)
                else:
                    curr_len = len(curr)
                    print(curr_len)
                    if curr_len > perm_len:
                        perm_len = curr_len
                        perm = curr

                        d = {}
                    break

        return perm_len


sol = Solution()
print(sol.lengthOfLongestSubstring('pwwkew'))
