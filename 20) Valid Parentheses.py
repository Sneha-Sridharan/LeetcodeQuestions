class Solution:
    def isValid(self, s):
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
            
