class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        maxcount=-1
        sub=""
        i=0
        while(i<len(s)):
            if s[i] in sub:
                sub=sub[1:]
            else:
                sub=sub+s[i]
                if (len(sub))>maxcount:
                    maxcount=len(sub)
                i=i+1
        return maxcount
