class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        mx = []

        for i in range (len(nums)):
            while dq and nums[dq[-1]] <= nums[i] :
                dq.pop()
            if dq and dq[0] <= i - k:
                dq.popleft()
            dq.append(i)
            if i >= k-1:
                mx.append(nums[dq[0]])
        return mx