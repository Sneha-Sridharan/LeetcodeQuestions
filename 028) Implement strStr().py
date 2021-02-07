class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle=="":
            return 0
        leng = len(needle)
        for i in range(0,len(haystack)-leng+1):
            if needle==haystack[i:i+leng]:
                return i
        return -1