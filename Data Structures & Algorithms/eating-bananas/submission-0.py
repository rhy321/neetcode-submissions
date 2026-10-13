class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)

        rate_k = r

        while l <= r:

            m = (l + r) // 2

            time = 0

            for x in piles:
                time += math.ceil(x / m)

            if time <= h:
                rate_k = m
                r = m - 1
            else:
                l = m + 1

        return rate_k