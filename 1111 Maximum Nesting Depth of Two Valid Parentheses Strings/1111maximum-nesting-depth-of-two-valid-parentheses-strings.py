class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        o = 0
        for b in seq:
            if b=="(":
                o+=1
                ans.append(o%2)
            if b==")":
                ans.append(o%2)
                o-=1
        return ans
        