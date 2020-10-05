lookup={}
def recur(n):  
    if n==1:
        return 1
    if n==2:
        return 2
    if n in lookup.keys():
        return lookup[n]
    else:
        lookup[n]=recur(n-1)+recur(n-2)
        return lookup[n]
class Solution:
    def climbStairs(self, n):
        return recur(n)
        