class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""

        T, window = {}, {}
        
        for c in t:
            T[c] = 1 + T.get(c, 0)

        have, need = 0, len(T)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in T and window[c] == T[c]:
                have += 1

            while have == need:
                windowLen = r - l + 1

                #update res if better
                if windowLen < resLen:
                    res = [l, r]
                    resLen = windowLen

                #pop from left
                window[s[l]] -= 1

                if s[l] in T and window[s[l]] < T[s[l]]:
                    have -= 1

                l += 1
            
        i, j = res

        return s[i:j+1] if resLen != float('inf') else ""