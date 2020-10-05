class Solution:
    def missingNumber(self, nums) :
        sums=sum(nums)
        n=len(nums)
        idealsum=n*(n+1)//2
        return idealsum-sums
        