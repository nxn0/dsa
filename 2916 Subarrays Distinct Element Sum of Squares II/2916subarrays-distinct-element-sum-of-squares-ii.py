class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        cnt,to=[0]*(n+1),[0]*(n+1) 
        l,a={},0
        for r,x in enumerate(nums):
            p=l.get(x,-1)
            c=s=0
            i=n-p-1
            while i:
                c+=cnt[i]
                s+=to[i]
                i-=i&-i
            a+=(n-r)*((r-p)**2-2*(s-p*c))
            i=n-p
            while i<=n:
                cnt[i]+=1
                to[i]+=p
                i+=i&-i
            l[x]=r
        return a%(10**9+7)
