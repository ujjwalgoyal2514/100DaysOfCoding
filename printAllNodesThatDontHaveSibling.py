"""Given a Binary Tree of n nodes, find all the nodes that don't have any siblings. You need to return a list of integers containing all the nodes that don't have a sibling in sorted order (Increasing).

Two nodes are said to be siblings if they are present at the same level, and their parents are the same.

Note: The root node can not have a sibling so it cannot be included in our answer.

Example 1:

Input :
       37
      /   
    20
    /     
  113 

Output: 
20 113
Explanation: 
Nodes 20 and 113 dont have any siblings.

Example 2:

Input :
       1
      / \
     2   3 

Output: 
-1
Explanation: 
Every node has a sibling.
Your Task:  
You don't need to read input or print anything. Complete the function noSibling() which takes the root of the tree as input parameter and returns a list of integers containing all the nodes that don't have a sibling in sorted order. If all nodes have a sibling, then the returning list should contain only one element -1.

Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(Height of the tree)

Constraints:
1 ≤ n ≤ 104"""
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def lets_try(root,l1):
    if root.left==None and root.right==None:
        return
    if root.left and root.right==None:
        l1.append(root.left.data)
    if root.right and root.left==None:
        l1.append(root.right.data)
    if root.left:
        lets_try(root.left,l1)
    if root.right:
        lets_try(root.right,l1)
def noSibling(head):
    l1=[]
    lets_try(head,l1)
    l1.sort()
    if l1:
        return l1
    return [-1]   