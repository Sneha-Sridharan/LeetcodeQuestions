class Solution(object):
    def myAtoi(self, str):
        str=str.strip()
        if str==[]:
            return 0
        result=0
        minus=False
        
        if len(str)>0 and str[0] not in ['+','-','0','1','2','3','4','5','6','7','8','9']:
            return 0
        if len(str)>0 and str[0]=='+':
            str=str[1:]
        elif  len(str)>0 and str[0]=='-':
            str=str[1:]
            minus=True
        for i in str:
            if i in ['0','1','2','3','4','5','6','7','8','9']:
                result=result*10 +int(i)
            else:
                break
        if minus:
            result*=-1
        if not (result<=pow(2,31)-1 and result>=-pow(2,31)):
            return -pow(2,31) if minus else pow(2,31)-1
        else:
            return result
            
                
