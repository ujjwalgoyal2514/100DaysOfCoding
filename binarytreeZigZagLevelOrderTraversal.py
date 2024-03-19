"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        que=[root]
        res=[]
        i=0
        while que:
            lev=[]
            temp=que
            que=[]
            for node in temp:
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                lev.append(node.val)
            if i%2==0:
                res.append(lev)
            else:
                res.append(lev[::-1])
            i+=1
        return res

            
            