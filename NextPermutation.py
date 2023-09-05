def matrix(a):
    j=-1
    for i in range(len(a)-1,-1,-1):
        if a[i-1]<a[i]:
            j=i-1
            break
    print(j)
    if j== -1:
        return reversed(a)
    for i in range(len(a)-1,j,-1):
          if  a[i]>a[j]:
             a[j],a[i]=a[i],a[j]
             break
    a[j+1:]=reversed(a[j+1:])   
    return a





print(matrix([1,3,2]))
                
        
            