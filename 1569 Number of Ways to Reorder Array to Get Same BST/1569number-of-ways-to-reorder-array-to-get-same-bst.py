class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        n=len(nums)
        e= [-1]*(n+2)
        for t,x in enumerate(nums):
            e[x]=t
        si,st=1,[0]
        for v in range(1,n+2):
            while e[st[-1]]>e[v]:
                st.pop()
                si*=v-st[-1]-1
            st.append(v)
        return (factorial(n)//si-1)%(10**9+7)