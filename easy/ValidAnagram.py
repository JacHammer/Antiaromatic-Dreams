# Minci
# time elapsed: 17 min
# submitted 3 times
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = dict()
        s = list(s)
        t = list(t)
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1
        print(s_dict)
        for i in range(len(t)):
            if t[i] in s_dict:
                if s_dict[t[i]] == 0:
                    return False
                else:
                    s_dict[t[i]] -= 1
            else:
                return False
        return True


sol = Solution()
s = 'anagram'
t = 'aangarm'
ans = sol.isAnagram(s, t)
print(ans)
