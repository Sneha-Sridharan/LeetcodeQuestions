class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}
        for i in range(len(nums)):
            ind[nums[i]] = i
            
        #print(dict1)
        for i in range(len(nums)-1):
            com = target - nums[i]
            if com in ind and i != ind[com]:
                    return [i,ind[com]]
