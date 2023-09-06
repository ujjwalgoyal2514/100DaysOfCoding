# def matrix(a):
   
#     maxi=max(a)
#     for i in range(0,len(a)):
#         s=0
#         for j in range(i,len(a)):
#             s=s+a[j]
#             maxi=max(maxi,s)
#     return maxi

# print(matrix([1,3,2]))


# *********************************optimal Approach**************************************
def kadane(a):
    max1=max(a)
    s=0
    start_index=end_index=-1
    for i in range(len(a)):
        if s==0:
            start_index=i
        s=s+a[i]
        if s>max1:
            max1=s
            end_index=i
        elif s<0:
            s=0
    return max1,a[start_index:end_index+1]
print(kadane([-2,-1,-3,4,2,3,5,-1]))