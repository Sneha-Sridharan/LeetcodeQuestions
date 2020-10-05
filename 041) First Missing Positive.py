class Solution(object):
    def firstMissingPositive(self, nums):
        flag=0
        n=1
        while flag==0:
            if n not in nums:
                flag=n
            n=n+1
        return flag
