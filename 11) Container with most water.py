class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg=0
        end=len(height)-1
        area=[]
        while beg<end:
            area.append((end-beg)*min(height[beg],height[end]))
            if height[beg]<=height[end]:
                beg+=1
            else:
                end-=1
        return max(area)
