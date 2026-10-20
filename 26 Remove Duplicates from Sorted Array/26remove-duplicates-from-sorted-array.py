class Solution:
    def removeDuplicates(self, a: list[int]) -> int:
        a[:] = sorted(set(a))
        return len(a)