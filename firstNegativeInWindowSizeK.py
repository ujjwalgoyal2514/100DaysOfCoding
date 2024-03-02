"""Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.

 

Example 1:

Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
 
Example 2:
Input : 
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0 
"""

def printFirstNegativeInteger( A, N, k):
    # code here
    i=0
    j=0
    lst=[]
    lst1=[]
    while j<N:
        if A[j]<0:
            c=1
            lst.append(A[j])
        if (j-i)+1<k:
            j+=1
        elif (j-i)+1==k:
            if len(lst)==0:
                lst1.append(0)
            else:
                lst1.append(lst[0])
                if lst[0]==A[i]:
                    lst.pop(0)
            i+=1
            j+=1
    return lst1