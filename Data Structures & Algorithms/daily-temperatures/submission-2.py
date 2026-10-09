class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:

        res = [0] * len(temps) #init accounts for 'holes'
        stk = [] #pair: [temp, index]

        for i, t in enumerate(temps):
            #pop from stack while the added temp > top element
            while stk and t > stk[-1][0]:
                stk_t, stk_i = stk.pop()
                res[stk_i] = (i - stk_i) #no. of days into res

            stk.append([t, i])

        return res