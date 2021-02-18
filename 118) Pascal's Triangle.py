
res=[]
def find(i):
    global res
    temp=[1]*i
    for val in range(1,i-1):
       # print(i-2,val,val-1,res)
        temp[val]=res[i-2][val-1]+res[i-2][val]
    return temp

    

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        global res
        res=[]
        if numRows==0:
            return []
        res.append([1])
        for i in range(2,numRows+1):
            res.append(find(i))
        return res
        