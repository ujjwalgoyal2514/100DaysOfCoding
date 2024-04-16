"""You are given an array arr of size n. You have to remove a subarray of size k , such that the difference between the maximum and minimum values of the remaining array is minimized.
Find the minimum value obtained after performing the operation of the removal of the subarray and return it.

Example 1:

Input:
n = 5
k = 3
arr = {1, 2, 3, 4, 5}
Output: 
1
Explanation: 
We can remove first subarray of length 3(i.e. {1, 2, 3}) then remaining array will be {4,5} and the difference of maximum and minimum element will be 1 i.e 5 - 4 = 1
Example 2:

Input:
n = 6
k = 3
arr = {2, 3, 1, 4, 6, 7}
Output: 
2
Explanation:
If we remove the subarray {2,3,1} then remaining array will be {4,6,7} and the difference  = 7-4 = 3
If we remove the subarray {3,1,4} then remaining array will be {2,6,7} and the difference  = 7-2 = 5
If we remove the subarray {1,4,6} then remaining array will be {2,3,7} and the difference  = 7-2 = 5
If we remove the subarray {4,6,7} then remaining array will be {2,3,1} and the difference  = 3-1 = 2
So the answer will be min(3,5,5,2) = 2
Your Task: 
You have to complete the function minimizeDifference( ), which takes two integers n and k and an integer array arr of size n. You have to return the minimum difference of maximum and minimum elements of the remaining array after removing one k length subarray of it.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
2 <= n <= 105
1 <= k <= n-1
0 <= arr[i] <= 109"""
class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        if k==n-1:
            return 0
        rit_min=[0]*n
        rit_max=[0]*n
        left_min=[0]*n
        left_max=[0]*n
        left_min[0]=left_max[0]=arr[0]
        for i in range(1,n):
            left_min[i]=min(left_min[i-1],arr[i])
            left_max[i]=max(left_max[i-1],arr[i])
        rit_min[-1]=rit_max[-1]=arr[-1]
        for i in range(n-2,-1,-1):
            rit_min[i]=min(rit_min[i+1],arr[i])
            rit_max[i]=max(rit_max[i+1],arr[i])
        ans=rit_max[k]-rit_min[k]
        i=0
        for j in range(k+1,n):
            ans=min(ans,max(left_max[i],rit_max[j])-min(left_min[i],rit_min[j]))
            i+=1
        ans=min(ans,left_max[i]-left_min[i])    
        return ans 