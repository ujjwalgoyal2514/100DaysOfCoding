def miss(a,b):
    count={}
    if(len(a)==0):
        return 0
    for i in a:
        if i in count:
            count[i]+=1
        else:
            count[i]=1    
    for j in b:
        if j in count:
            count[j]-=1
        else:
            count[j]=1
    for k in count:
        if count[k]==1:
            return k
        
        
        
d=miss([1,2,3,4,5,6,7],[3,7,2,1,4,6])
print(d)    





    
                            