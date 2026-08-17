class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0

        res = 1
        l = 0
        ss = set()

        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l+=1
            ss.add(s[r])
            res = max(res, r - l + 1)

        return res