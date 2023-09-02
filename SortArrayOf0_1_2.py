# Dutch National flag algorithm.
# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

# Examples
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Input: nums = [2,0,1]
# Output: [0,1,2]

# Input: nums = [0]
# Output: [0]

def matrix(a):
    low=0
    mid=0
    high=len(a)-1
    while(mid<=high):
        if a[mid]==0:
            a[low],a[mid]=a[mid],a[low]
            low+=1
            mid+=1
        elif(a[mid]==1):
            mid+=1
        else:
            a[mid],a[high]=a[high],a[mid]
            high-=1
    return a


print(matrix([0,2,1,2,0,1,2,1,2,1,0,0])        )        