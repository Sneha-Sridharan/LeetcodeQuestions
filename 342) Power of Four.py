import re
class Solution(object):
    def isPowerOfFour(self, num):
        if num<0:
            return False
        string =bin(num)        
        if re.findall(r'0b0*1(00)+$',string) or num==1:
            return True
        else:
            return False
        
        
        