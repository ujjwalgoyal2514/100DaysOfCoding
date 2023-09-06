def findMissingRepeatingNumbers(a):
    # Write your code here
    count={}
    f=0
    s1=0
    s=[*range(1,len(a)+1)]
    for i in range(len(a)):
        if a[i] in count:
            count[a[i]]+=1
        else:
            count[a[i]]=1
        if s[i] not in a:
            s1=s[i]
    for k in count:
        if count[k]>1:
            f=k
    return ({f,s1})

print(findMissingRepeatingNumbers([1,2,1]))


