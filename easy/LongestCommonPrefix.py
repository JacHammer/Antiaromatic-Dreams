from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = ''
        if strs != []:
            strs.sort(key=lambda s: len(s))
        else:
            return temp

        for i in range(len(strs[0])):
            for s in strs:
                if strs[0][i] != s[i]:
                    return temp
            temp += strs[0][i]
        return temp


sol = Solution()
strs = ['flower', '']
print(sol.longestCommonPrefix(strs))
