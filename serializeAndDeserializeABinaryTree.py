"""Serialization is to store a tree in an array so that it can be later restored and deserialization is reading tree back from the array. Complete the functions

serialize() : stores the tree into an array a and returns the array.
deSerialize() : deserializes the array to the tree and returns the root of the tree.
Note: Multiple nodes can have the same data and the node values are always positive integers. Your code will be correct if the tree returned by deSerialize(serialize(input_tree)) is same as the input tree. Driver code will print the in-order traversal of the tree returned by deSerialize(serialize(input_tree)).

Example 1:

Input:
      1
    /   \
   2     3
Output: 
2 1 3
Example 2:

Input:
         10
       /    \
      20    30
    /   \
   40  60
Output: 
40 20 60 10 30
Your Task:
The task is to complete two functions serialize which takes the root node of the tree as input and stores the tree into an array and deSerialize which deserializes the array to the original tree and returns the root of it.

Expected Time Complexity: O(Number of nodes).
Expected Auxiliary Space: O(Number of nodes).

Constraints:
1 <= Number of nodes <= 104
1 <= Data of a node <= 109
"""
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        
        def inorder(root , res):
            if root:
            
                inorder(root.left , res)
                res.append(root.data)
                inorder(root.right ,res)
        res = []
        inorder(root ,res)
        
        return res
        #code here
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        
        
        def helper(a, l , r):
            if l > r:
                return 
            idx = (l+r)//2
            
            root = Node(a[idx])
            
            root.left = helper(a , l , idx-1)
            root.right = helper(a, idx +1 , r)
            return root 
        return helper(a, 0 , len(a)-1)