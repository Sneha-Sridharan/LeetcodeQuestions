class Solution(object):
    def firstUniqChar(self, s):
        dict={}
        for i,c in enumerate(s):
            #print(dict)
            if c in dict.keys():
                dict[c][1]+=1
            else:
                dict[c]=[i,1]
        #print(dict)
        for i in dict.keys():
            if dict[i][1]==1:
                return dict[i][0]
        return -1
        
        # for i in range(len(s)):
        #     if s.count(s[i])==1:
        #         return i
        # return -1
        