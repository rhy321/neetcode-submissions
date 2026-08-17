class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        # while r in range(len(numbers) - 1) and numbers[r] < target:
        #     r += 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            elif sum == target:
                return [l+1,r+1]
