class Solution:
    def magicalString(self, n: int) -> int:
        s='122'
        count=2
        m=2
        while len(s)<n:
            temp=int(s[count])
            if s[m]=='1':
                s=s+'2'*temp
            else:
                s = s + '1' * temp
            m+=int(s[count])
            count+=1
        s=s[:n]
        num=s.count('1')
        return num
