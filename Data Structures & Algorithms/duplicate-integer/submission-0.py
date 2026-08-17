class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for no in nums:
            if no in s:
                return True
            s.add(no)
        return False
