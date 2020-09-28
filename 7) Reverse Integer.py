#using strings:
class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        if x[0]=='-':
            rev='-' + x[1:][::-1]
        else:
            rev=x[::-1]
        rev=int(rev)
        if rev>(2**31-2) or rev<-2**31:
            return 0
        return rev

#without using strings:
class Solution(object):
    def reverse(self, x):
        rev=0
        neg=0
        if x<0:
            x=-x
            neg=1
        while x!=0:
            rem=x%10
            rev=rev*10+rem
            if rev>=2**31 or rev<(-2**31):
                return 0
            x=x/10
        if neg==1:
            rev=-rev
        return rev
