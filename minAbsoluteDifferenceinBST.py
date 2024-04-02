"""Given a binary search tree having n (n>1) nodes, the task is to find the minimum absolute difference between any two nodes.

Example 1:

Input:
Input tree

Output:
10
Explanation:
There are no two nodes whose absolute difference is smaller than 10.
Example 2:

Input:
Input tree

Output:
20
Explanation:
There are no two nodes whose absolute difference is smaller than 20.
Your Task:
You don't have to take any input. Just complete the function absolute_diff() , that takes root as input and return minimum absolute difference between any two nodes.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(Height of tree)

Constraints:
2 <= n <= 105
1 <= Node->data <= 109"""
class Solution:
    def absolute_diff(self,root):
        # Your code here
        temp = []
        def solve(root):
            if not root:
                return
            solve(root.left)
            temp.append(root.data)
            solve(root.right)
        solve(root)
        ans = float("inf")
        for i in range(1,len(temp)):
            ans = min(ans, abs(temp[i]-temp[i-1]))
        return ans