class Solution:
    def maxProfit(self, p: List[int]) -> int:
        res = 0
        i, j = 0,1

        while i<j and j in range(len(p)):
            while p[i] > p[j] and j in range(len(p)-1):
                i = j
                j+=1
            profit = p[j]-p[i]
            res = max(profit,res)
            j+=1
        return res