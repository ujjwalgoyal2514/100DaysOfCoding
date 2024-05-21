"""Given a sorted array of unique elements in increasing order, arr[] of n integers, and a value x. Find the K closest elements to x in arr[].
Keep the following points in mind:

If x is present in the array, then it need not be considered.
If two elements have the same difference as x, the greater element is prioritized.
If sufficient elements are not present on the right side, take elements from the left and vice versa.
 
Example 1:

Input:
n = 13
arr[] = {12, 16, 22, 30, 35, 39, 42, 
         45, 48, 50, 53, 55, 56}
k = 4, x = 35
Output: 39 30 42 45
Explanation: 
First closest element to 35 is 39.
Second closest element to 35 is 30.
Third closest element to 35 is 42.
And fourth closest element to 35 is 45.

Example 2:

Input:
n = 5
arr[] = {1, 2, 3, 6, 10}
k = 3, x = 4
Output: 3 6 2
Explanation: 
First closest element is 3.
There are two elements 2 and 6 for which 
the difference with 4 is same i.e. 2.
So first take greatest number 6 
then the lower number 2.

Your Task:
You don't need to read input or print anything. Complete the function printKClosest() which takes arr[], n, k, and x as input parameters and returns an array of integers containing the K closest elements to x in arr[].


Expected Time Complexity: O(log n + k)
Expected Auxiliary Space: O(k)


Constraints:
1 ≤ n ≤ 105
1 ≤ k ≤ n
1 ≤ x ≤ 106
1 ≤ arr[i] ≤ 106

 """
 from bisect import bisect_left as lower, bisect_right as upper
class Solution:
    def printKClosest(self, arr, n, k, x):
        sorted(arr)
        ans=[]
        u = upper(arr, x)
        l = lower(arr, x); 
        l-=1
        while(l>=0 and arr[l] == x): l-=1
        if l>=0 and arr[l]==x: l=-1
        ok=False; ok1=False; d=n+1; d1=n+1;
        while(len(ans)!=k):
            if l>=0: ok=True
            else: ok=False
            if u<n: ok1=True
            else: ok1=False
            if not ok and not ok1: break
            if ok : d=abs(x-arr[l])
            else: d=100000000000000000000000
            if ok1: d1=abs(x-arr[u])
            else: d1=100000000000000000000000
            i = min(d, d1)
            if i==d1: ans.append(arr[u]); u+=1;
            else: ans.append(arr[l]); l-=1;
        return ans