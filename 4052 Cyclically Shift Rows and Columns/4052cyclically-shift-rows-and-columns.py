class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], row: list[int], col: list[int]) -> list[list[int]]:
        n = len(grid)
        temp = [[0] * n for _ in range(n)]
        for i in range(n):
            k=row[i]%n
            for j in range(n):
                nj = (j-k+n) %n
                temp[i][nj] = grid[i][j]
        aaaaaa = [[0] * n for _ in range(n)]
        for j in range(n):
            k = col[j]%n
            for i in range(n):
                ni = (i-k+n)%n
                aaaaaa[ni][j] = temp[i][j]
        return aaaaaa
                
        
            