class Solution:
    def firstStableIndex(self, A: list[int], k: int) -> int:
        msf = -1
        cand = m =0
        for i, x in enumerate(A):
            msf = max(msf, x)

            if i == cand:
                m = msf
            if x < m - k:
                cand = i+1
        return cand if cand < len(A) else -1

        