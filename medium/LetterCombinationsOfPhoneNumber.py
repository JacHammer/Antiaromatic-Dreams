# Minci
# time elapsed: > 1d
# submitted 1 time


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {2: 'abc', 3: 'def', 4: 'ghi', 5: "jkl", 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        if digits == '':
            return []
        if len(digits) == 1:
            return list(letter_dict[int(digits[0])])
        prev = self.letterCombinations(digits[:-1])
        last = letter_dict[int(digits[-1])]
        ret = []
        for x in prev:
            for y in last:
                ret.append(x+y)
        return ret
        #return [x + y for x in prev for y in last]

sol = Solution()
ans = sol.letterCombinations('234')
print(ans)