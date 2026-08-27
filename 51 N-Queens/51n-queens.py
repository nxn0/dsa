class Solution(object):
    def solveNQueens(self, n):
        def dfs(qns, xydif, xysum):
            p = len(qns)
            if p==n:
                result.append(qns)
                return None
            for q in range(n):
                if q not in qns and p-q not in xydif and p+q not in xysum:
                    dfs(qns+[q],xydif+[p-q],xysum+[p+q])
        result = []
        dfs([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
        