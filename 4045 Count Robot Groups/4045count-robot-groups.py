class Solution:
    def countGroups(self, pos: list[int], sp: list[int], dist: int) -> int:
        p2 = s2 = inf
        res = 0
        for p,s,in zip(pos[::-1], sp[::-1]):
            if p2 - p > dist and s<= s2:
                res += 1
                s2 = s
            p2 = p
        return res
        