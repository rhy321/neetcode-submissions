class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        mx = 0

        for i, h in enumerate(heights):

            start = i

            while stk and stk[-1][1] > h:
                eff_idx, height = stk.pop()
                mx = max(mx, (i - eff_idx) * height)
                start = eff_idx

            stk.append((start, h))

        for eff_idx, h in stk:
            mx = max(mx, (len(heights) - eff_idx) * h)

        return mx