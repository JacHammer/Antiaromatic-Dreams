# Minci
# time elapsed:
# submitted


from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:

        count = []
        for i in range(num+1):
            num_bin_string = str(bin(i))
            num_bin_string = num_bin_string[1:len(num_bin_string)]
            count.append(num_bin_string.count('1'))
        return count


sol = Solution()
ans = sol.countBits(59990)
print(ans)