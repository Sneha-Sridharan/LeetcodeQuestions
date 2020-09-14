class Solution:
    
    def insert(self,intervals,newInterval):
        intervals.sort(key=lambda x:x[0])
        print(intervals)
        locatex=-1
        locatey=-1
        xinBetween=False
        yinBetween=False
        prevHigh=-1
        last=True
        x,y=newInterval
        for i in range(len(intervals)):
            
            a,b=intervals[i]   
            if x>a and y>a and x>b and y>b:
                last=True
            else:
                last=False
            #locate x
            if x>=a and x<=b:
                locatex=i
            if i!=0 and x<a and x>prevHigh:
                xinBetween=True
                locatex=i
            #locate y
            if y>=a and y<=b:
                locatey=i
            if i!=0 and y<a and y>prevHigh:
                yinBetween=True
                locatey=i                
            prevHigh=b
         
        print(locatex,locatey,xinBetween,yinBetween,last)
        if locatey==-1 and locatex!=-1:
            locatey=len(intervals)-1
            intervals[locatey][1]=y
        if last and locatex==-1 and locatey==-1:
            intervals.append([x,y])
            return intervals
        
        if locatex==-1 and locatey!=-1:
            locatex=0
            intervals[locatex][0]=x
            return intervals
            
            
            
        if locatex==-1 and not last:
            intervals[:0]=[[x,y]]
            return intervals
            
            
            
            
        
        if not xinBetween and not yinBetween:
            intervals[locatex][1]=intervals[locatey][1]
            intervals=intervals[:locatex+1]+intervals[locatey+1:]
        
        if xinBetween and yinBetween:            
            intervals[locatex:locatey]=[[x,y]]
            
        if yinBetween:
            intervals[locatex][1]=y
            intervals[locatex+1:locatey]=[]
            
        if xinBetween:
            intervals[locatex][0]=x
            intervals[locatex+1:locatey]=[]
        
        return intervals
