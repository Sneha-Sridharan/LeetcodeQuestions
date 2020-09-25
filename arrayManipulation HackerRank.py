def arrayManipulation(n, queries):
    arr=[0]*n
    for i in range(len(queries)):
        arr[queries[i][0]-1]+=queries[i][2]
        if queries[i][1]!=n:
            arr[queries[i][1]]-=queries[i][2]
    sumel=0   
    maxim=-1
    for i in range(n):
        sumel+=arr[i]
        if sumel>maxim:
            maxim=sumel
    return maxim
