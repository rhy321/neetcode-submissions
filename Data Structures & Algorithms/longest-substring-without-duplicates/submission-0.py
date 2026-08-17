class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        max_cnt = 0
        i=0
        j = 1
        if len(s) == 0: return 0
        seen.add(s[0])

        while j<len(s):
            if s[j] in seen:
                max_cnt = max(max_cnt, len(seen))
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i+=1
                i+=1
            else:
                seen.add(s[j])
            j+=1
        max_cnt = max(max_cnt, len(seen))
        return max_cnt