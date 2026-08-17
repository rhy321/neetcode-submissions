class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            ar = min(heights[l], heights[r]) * (r - l)

            res = max(ar, res)

            if heights[l] < heights[r]: l += 1
            elif heights[l] >= heights[r]: r -= 1


        return res