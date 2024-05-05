"""Given a binary tree having n nodes, find the vertical sum of the nodes that are in the same vertical line. Return all sums through different vertical lines starting from the left-most vertical line to the right-most vertical line.

Example 1:

Input:
       1
    /    \
  2      3
 /  \    /  \
4   5  6   7
Output: 
4 2 12 3 7
Explanation:
The tree has 5 vertical lines
Line 1 has only one node 4 => vertical sum is 4.
Line 2 has only one node 2 => vertical sum is 2.
Line-3 has three nodes: 1,5,6 => vertical sum is 1+5+6 = 12.
Line-4 has only one node 3 => vertical sum is 3.
Line-5 has only one node 7 => vertical sum is 7.
Example 2:

Input:
          1
         /
        2
       /
      3
     /
    4
   /
  6
 /
7
Output: 
7 6 5 4 3 2 1
Explanation:
There are seven vertical lines each having one node.
Your Task:
You don't need to take input. Just complete the function verticalSum() that takes root node of the tree as parameter and returns an array containing the vertical sum of tree from left to right.

Expected Time Complexity: O(nlogn).
Expected Auxiliary Space: O(n).

Constraints:
1<=n<=104
1<= Node value <= 105
"""
# Node Class:
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Complete the function below
    def verticalSum(self, root):
        #:param root: root of the given tree.
        
        #code here
        mapp = {}
        def dfs(node, pos):
            if not node:
                return
            dfs(node.left,pos-1)
            mapp[pos] = mapp.get(pos, 0)+node.data
            dfs(node.right,pos+1)
        dfs(root,0)
        arr = []
        for key, val in mapp.items():
            arr.append([key,val])
        arr.sort()
        return [val for i, val in arr]