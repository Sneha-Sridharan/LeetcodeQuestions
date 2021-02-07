class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        strs.sort()
        prefix=""
        for i in range(1,len(strs[0])+1):
            if strs[0][:i]==strs[-1][:i]:
                prefix=strs[0][:i]
            else:
                break
        return prefix