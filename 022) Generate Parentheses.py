def isValid(s):
        stack=[]
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                if stack==[]:
                        return False
                if char==')':                    
                    if stack.pop()!='(':
                        return False                    
                if char==']':
                    if stack.pop()!='[':
                        return False                    
                if char=='}':
                    if stack.pop()!='{':
                        return False
        if stack!=[]:
            return False
        return True
res=""
finalAns=[]
def recur(i,n):
    global res
    if i==2*n:
        print(res,isValid(res))
        if isValid(res):
            finalAns.append(res)
        return
    res=res[::]+'('
    recur(i+1,n)
    res=res[:-1]
    res=res[::]+')'
    recur(i+1,n)
    res=res[:-1]
    
class Solution:
  
    
    def generateParenthesis(self, n):
        global finalAns
        finalAns=[]
        recur(0,n)
        return finalAns
   
        
    
        
        
