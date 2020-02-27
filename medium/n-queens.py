from typing import List


class Solution():
    def solveNQueens(self, n: int) -> List[List[str]]:
        sols = []

        def backtrack(pos, row):
            if len(pos) == n and row == n:
                sols.append(pos)
            for col in range(n):
                # print([row != row1 and col != col1 and abs(row - row1) != abs(col - col1) for row1, col1 in pos])
                truth_list = [True]
                for row1, col1 in pos:
                    if row != row1 and col != col1 and abs(row - row1) != abs(col - col1):
                        truth_list.append(True)
                    else:
                        truth_list.append(False)
                if len(list(set(truth_list))) == 1:
                    backtrack(pos + [(row, col)], row + 1)

        backtrack([], 0)
        return [
            [''.join('Q' if (i, j) in sol else '.' for i in range(n)) for j in range(n)]
            for sol in sols
        ]


sol = Solution()
print(sol.solveNQueens(5))
