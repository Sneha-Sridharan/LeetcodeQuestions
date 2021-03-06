class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length=len(nums1)
        mid1=int((length-1)/2)
        mid2=int(length/2)
        if length%2==0:
            median = (nums1[mid2]+nums1[mid2-1])/2
        else:
            median = nums1[mid1]
        return median