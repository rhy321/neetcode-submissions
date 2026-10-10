class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p,s] for p, s in zip(position, speed)]

        stk = []

        #reverse sorted order to go from left to right
        for p, s in sorted(pair)[::-1]: 

            stk.append((target - p) / s)

            #check for collisions
            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop() #remove the car behind because its functionally the same as the one ahead so it'd collide with the same stuff as the one ahead anyway

        return len(stk)