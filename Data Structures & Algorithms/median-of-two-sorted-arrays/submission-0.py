class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArr = nums1 + nums2
        newArr.sort()
        length = len(newArr)
        if length % 2 == 0:
            mid = ((length//2)+(length//2+1))/2
            return mid
        else:
            mid = (length//2)+1
            return mid

