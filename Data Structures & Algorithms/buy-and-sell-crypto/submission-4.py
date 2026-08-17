class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l,r=0,1
        res=0

        while r < len(p):
            if p[l]<p[r]:
                profit=p[r]-p[l]
                res=max(res,profit)
            else:
                l=r
            r+=1
        return res