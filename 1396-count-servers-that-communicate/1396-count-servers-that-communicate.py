class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        r = [sum(row) for row in grid]
        c= [sum(col) for col in zip(*grid)]

        ans =0
        for i,row in enumerate(grid):
            for j, server in enumerate(row):
                if server and r[i] + c[j] > 2:
                    ans += 1
        return ans