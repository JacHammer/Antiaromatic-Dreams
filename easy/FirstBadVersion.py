# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version >= 4:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n):
        lo = 0
        hi = n
        mid = n // 2
        while lo < hi:
            if isBadVersion(mid):
                hi = mid
                mid = lo + (hi - lo) // 2
            else:
                lo = mid + 1
                mid = lo + (hi - lo) // 2
        return mid

sol = Solution()
print(sol.firstBadVersion(5))