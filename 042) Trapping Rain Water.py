class Solution:
    def trap(self, height: List[int]) -> int:
        if height==[]:
            return 0
        leftmax=[height[0]]
        lastind=len(height)-1
        rightmax=[0]*(lastind+1)
        rightmax[lastind]=height[lastind]
        i=1
        j=lastind-1
        water=0
        while i<=lastind and j>=0:
            if leftmax[i-1]<height[i]:
                leftmax.append(height[i])
            else:
                leftmax.append(leftmax[i-1])
            if rightmax[j+1]<height[j]:
                rightmax[j]=height[j]
            else:
                rightmax[j]=rightmax[j+1]
            i+=1
            j-=1
        for i in range(1,lastind+1):
            water+=min(leftmax[i],rightmax[i])-height[i]
        return water
