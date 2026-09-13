class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        e = 0
        st = []
        for x in nums:
            while st and st[-1] > x:
                st.pop()
            e+=bisect_left(st,x)
            st.append(x)
        return e