class Solution:
    def minQueenMoves(self, sc: list[int], tg: list[int]) -> int:
        sr, src = sc
        tr, tgt = tg

        if sr == tr and src == tgt:
            return 0

        rd = abs(tr-sr)
        cd = abs(tgt-src)

        if sr == tr or src == tgt or rd ==cd:
            return 1
        return 2