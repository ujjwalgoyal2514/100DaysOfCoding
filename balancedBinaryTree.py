"""Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104"""
class Solution:
    def helper(self,root):
            if root is None:
                return 0
            lh=self.helper(root.left)
            if lh==-1:return -1
            rh=self.helper(root.right)
            if rh==-1:return -1
            if abs(lh - rh)>1:return -1
            return 1 + max(lh,rh)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=self.helper(root)
        if ans!=-1:
            return True
        else:
            return False
