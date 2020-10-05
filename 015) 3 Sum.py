#Passed 315/318 cases. Last 3 cases - Time Limit Exceeded. See if you can come up with a more optimal solution.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l=[]
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                temp=-(nums[i]+nums[j])
                if temp in nums[j+1:]:
                    sortl=sorted([nums[i],nums[j],temp])
                    if sortl not in l:
                        l.append(sortl)
                j=j+1
            i=i+1
        return l
