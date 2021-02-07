class Solution(object):
    def firstMissingPositive(self, nums):
        if nums==[]:
            return 1
        nums.sort()
        i=0
        flag=0
        while nums[i]<=1:
            if nums[i]==1:
                flag=1
            i+=1
            if i>=len(nums):
                break
        if flag==0:
            return 1
        if i==len(nums):
            return 2
        for j in range(i,len(nums)):
            if nums[j]-nums[j-1]>1:
                return nums[j-1]+1
        return nums[j]+1
