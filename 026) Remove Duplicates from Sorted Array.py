# 1 - More appropriate but slower as we remove the duplicates here:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i-1)
            else:
                i+=1
        return len(nums)
                    
# (OR)

# 2 - Faster as we just shift the array to get the first j elements to be unique

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                j += 1
                nums[j] = nums[i]
                
        j += 1
        return j