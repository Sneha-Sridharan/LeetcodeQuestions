class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count=0
        neg=(dividend<0 and divisor>=0) or (dividend>=0 and divisor<0)
        if dividend<0:
            dividend = -dividend
        if divisor<0:
            divisor = -divisor
        while dividend>=divisor:
            i=1
            temp=divisor
            while dividend>=temp:
                dividend-=temp
                count+=i
                temp+=temp
                i+=i
        if (neg and count>2**31) or (not neg and count>=2**31):
            return 2**31-1
        if neg==1:
            return -count
        return count