"""
Given a Binary Tree of nodes, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

Example 1:

Input:
       1
    /     \
   2       3
Output: 
1 2 
1 3 
Explanation: 
All possible paths:
1->2
1->3
Example 2:

Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 
10 20 40 
10 20 60 
10 30 
"""
class Solution:
    def Paths(self, root: Optional['Node']) -> List[List[int]]:
        if not root:
            return []

        paths = []
        self.dfs(root, [], paths)
        return paths

    def dfs(self, node, path, paths):
        # Add current node to the path
        path.append(node.data)

        # If it's a leaf node, add the current path to paths
        if not node.left and not node.right:
            paths.append(path[:])

        # Recur for left and right subtrees
        if node.left:
            self.dfs(node.left, path, paths)
        if node.right:
            self.dfs(node.right, path, paths)

        # Backtrack: Remove the current node from the path
        path.pop()