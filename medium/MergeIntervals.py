# Minci
# Time elapsed: 20 min
# Submitted: 3 times


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        if intervals == []:
            return []
        interval_list = [intervals.pop(0)]

        while intervals != []:
            if interval_list == []:
                interval_list.append(intervals.pop(0))
            elif interval_list[-1][-1] >= intervals[0][0]:
                interval_list[-1][-1] = max(intervals.pop(0)[1], interval_list[-1][-1])
            else:
                interval_list.append(intervals.pop(0))
        return interval_list


sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
ans = sol.merge(intervals)
print(ans)