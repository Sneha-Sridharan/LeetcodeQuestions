class Solution(object):
    def countBits(self, num):
        list1=[]
        for i in range(num+1):
            list1.append(bin(i).count('1'))
            
        return list1
        