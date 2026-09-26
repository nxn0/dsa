class Solution:
    def canTransform(self, src: list[int], tgt: list[int]) -> bool:
        return sum(src) == sum(tgt)