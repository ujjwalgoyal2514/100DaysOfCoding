"""You are standing on a point (x, y) and you want to go to origin (0, 0) by taking steps either left or up i.e. from each point you are allowed to move either in (x-1, y) or (x, y-1). Find the number of paths from point to origin.

Example 1:

Input:
x = 3, y = 0 
Output: 
1
Explanation: Path used was -  (3,0)  --> ( 2,0) --> (1,0) --> (0,0).We can see that there is no other path than this, so we return 1.
Example 2:

Input:
x = 3, y = 6
Output: 
84 
Explanation:
There are total 84 possible paths.
Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function ways() that takes integer x and  y as parameters and returns the total number of paths from point(x,y) to the origin(0,0) % 1000000007.

Expected Time Complexity: O(x*y).
Expected Auxiliary Space: O(x*y).

Constraints:
1 ≤ x, y ≤ 500"""
class Solution:
    def ways(self, x, y):
        mod = 1000000007
        
        # Initialize dp array with zeros
        dp = [0] * (min(x, y) + 1)

        # Base case: There is only one path to reach the origin (0, 0)
        dp[0] = 1

        # Calculate the number of paths for each point along the diagonal
        for i in range(1, min(x, y) + 1):
            dp[i] = (dp[i - 1] * (x + y - i + 1) * pow(i, mod - 2, mod)) % mod

        return dp[min(x, y)]