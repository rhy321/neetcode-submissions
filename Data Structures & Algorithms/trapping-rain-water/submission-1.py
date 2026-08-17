class Solution:
    def trap(self, h: List[int]) -> int:
        if not h: return 0

        l, r = 0, len(h) - 1
        leftmax, rightmax = h[l], h[r]
        res = 0

        while l<r:
            if leftmax < rightmax: 
                l+=1
                leftmax = max(leftmax, h[l])
                res += leftmax - h[l]
            else:
                r-=1
                rightmax = max(rightmax, h[r])
                res += rightmax - h[r]

        return res