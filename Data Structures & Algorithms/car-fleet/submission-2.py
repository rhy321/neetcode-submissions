class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:      
        
        pair = [[p,s] for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stk = []

        #reverse sorted order to go from left to right
        for p, s in pair: 

            stk.append((target - p) / s)

            #check for collisions
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop() 

        return len(stk)