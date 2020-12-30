class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        n=len(nums)
        li=set()
        for i in range(n-1):  
            l = i + 1
            r = n - 1
            if i!=0 and nums[i]==nums[i-1]:
                continue
            x = nums[i] 
            while (l < r): 
                sumli=x + nums[l] + nums[r]
                if (sumli == 0):
                    trip=(x, nums[l], nums[r])
                    li.add(trip)
                    l+=1
                    r-=1
                elif (sumli < 0): 
                    l+=1 
                else: 
                    r-=1
        return li
