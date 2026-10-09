class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:

        res = [0] * len(temps) #init accounts for 'holes'
        stk = []

        for i, t in enumerate(temps):
            #pop from stack while the added temp > top element
            while stk and t > temps[stk[-1]]:
                stk_i = stk.pop()
                res[stk_i] = (i - stk_i) #no. of days into res

            stk.append(i)

        return res