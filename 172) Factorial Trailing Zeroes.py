class Solution:
    def trailingZeroes(self, n: int) -> int:
        i=5
        c=0
        while i<=n:
            c+=n//i
            i*=5
        return c
            
        