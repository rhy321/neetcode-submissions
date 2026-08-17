class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0

        res = 1
        l,r = 0, 1
        ss = s[0]

        while r < len(s):
            while s[r] in ss and l<r:
                l+=1
                ss = s[l:r]
            ss += s[r]
            res = max(res, r - l + 1)
            r+=1

        return res