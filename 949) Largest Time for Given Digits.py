#pretty lame and brute force
def fixResult(index,result,List):
        flag=False
        if index==0:
            for i in [2,1,0]:
                if i in List:
                    if i!=2:
                        result+=str(i)
                        List.remove(i)
                        flag=True
                        return (List,result,flag)
                        
                    if i==2:
                        l3=False
                        l5=False
                        List.remove(2)
                        for k in List:                            
                            if k<=3 and not l3:
                                l3=True
                                continue
                            if k<=5:
                                l5=True
                                continue
                        List.append(2)
                        print(l3,l5)
                        if l3 and l5:
                            result+=str(i)
                            List.remove(i)
                            flag=True
                            return (List,result,flag)               
            return (List,result,flag)
        if index==1:
            for i in sorted(List,reverse=True):
                temp=result+str(i)
                if int(temp)<24:
                    List.remove(i)
                    flag=True
                    return (List,temp,flag)
            return (List,result,flag)
        if index==2:
            for i in range(5,-1,-1):
                if i in List:
                    List.remove(i)
                    flag=True
                    result+=":"+str(i)
                    result+=str(List[0])                    
                    return ([],result,flag)
            return (List,result,flag)
        
                    
    
    
                
           
class Solution:
    
    def largestTimeFromDigits(self, List):
        result=""
        index=0
        while index<3:
            List,result,flag=fixResult(index,result,List)
            print(List,result)
            if flag:
                index+=1
            else:
                return ""
        return result
            
        
            
        
        
        
        