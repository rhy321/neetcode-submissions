class Solution:
    def checkBrack(self, s):
        if (s == ']'): return ('[')
        if (s == ')'): return ('(')
        if (s == '}'): return ('{')

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        opening = ['(', '{', '[']
        #closing = [')', '}', ']']
        stk = []

        for i in range(len(s)):
            if s[i] in opening:
                stk.append(s[i])

            else:
                if stk and stk.pop() == self.checkBrack(s[i]):
                    continue
                else:
                    return False

        return not stk 
    
        