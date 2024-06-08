"""You have given two sorted arrays arr1[] & arr2[] of distinct elements. The first array has one element extra added in between. Return the index of the extra element.

Note: 0-based indexing is followed.

Examples

Input: n = 7, arr1[] = {2,4,6,8,9,10,12}, arr2[] = {2,4,6,8,10,12}
Output: 4
Explanation: In the first array, 9 is extra added and it's index is 4.
Input: n = 6, arr1[] = {3,5,7,8,11,13}, arr2[] = {3,5,7,11,13}
Output: 3
Explanation: In the first array, 8 is extra and it's index is 3.
Expected Time Complexity: O(log n).
Expected Auxiliary Space: O(1).

Constraints:
2<=n<=105
1<=a[i],b[i]<=106

"""
class Solution:
    def findExtra(self,n,a,b):
        #add code here
        i=0
        j=0
        while i<n and j<n-1:
            if a[i]!=b[j]:
                return i
            i+=1
            j+=1
        while i<n:
            if a[i] not in b:
                return i
            i+=1