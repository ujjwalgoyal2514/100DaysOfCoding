"""Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

Examples:

Input: arr[] = {1,2,3,7,5}, n = 5, s = 12
Output: 2 4
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = {1,2,3,4,5,6,7,8,9,10}, n = 10, s = 15,
Output: 1 5
Explanation: The sum of elements from 1st to 5th position is 15.
Input: arr[] = {7,2,1}, n = 3, s = 2
Output: 2 2
Explanation: The sum of elements from 2nd to 2nd position is 2.
Input: arr[] = {5,3,4}, n = 3, s = 2
Output: -1
Explanation: There is no subarray with sum 2
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:

0 <= arr[i] <= 109
1 <= n <= 105
0 <= s <= 109"""
class Solution:
    def subArraySum(self,arr, n, s): 
        curSum = 0
        left = 0
        right = 0
        while (right<n):
            curSum +=arr[right]
            while curSum>s and left<right :
                curSum -=arr[left]
                left+=1
            if(curSum==s):
                return [left+1,right+1]
            right+=1
        return [-1] 