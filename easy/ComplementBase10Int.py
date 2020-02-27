# Minci
# time elapsed: 22 min
# submitted 1 time


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary_representation = bin(N)
        len_bit = len(binary_representation) - 2
        comp = N ^ (2 ** len_bit - 1)
        return comp


sol = Solution()
ans = sol.bitwiseComplement(10)
print(ans)