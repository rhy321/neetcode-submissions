class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        arr = nums1 + nums2
        arr.sort()

        print(arr)
        half = (len(arr) - 1) // 2

        if len(arr) % 2 != 0:
            return arr[half]

        else:
            return (arr[half] + arr[half + 1]) / 2