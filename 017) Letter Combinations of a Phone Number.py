class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digletter={'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        l=[]
        if digits=="":
            return l
        l=[i for i in digletter[digits[0]]]
        if len(digits)==1:
            return l
        for i in range(1,len(digits)):
            if digits[i]!='1':
                l=[k+j for k in l for j in digletter[digits[i]]]
        return l
