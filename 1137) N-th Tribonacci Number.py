lookup={}
def triboRecur(N):
    if N==0:
        return 0
    if N==1:
        return 1
    if N==2:
        return 1
    if N in lookup.keys():
        return lookup[N]
    else:
        lookup[N]=triboRecur(N-1)+triboRecur(N-2)+triboRecur(N-3)
        return lookup[N]

class Solution:
    def tribonacci(self, n):
        res=triboRecur(n)
        return res
        