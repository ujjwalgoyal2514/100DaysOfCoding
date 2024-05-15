"""A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Example 1:

Input:
LinkedList: 4->5->6
Output: 457
Explanation: 4->5->6 represents 456 and when 1 is added it becomes 457. 
Example 2:

Input:
LinkedList: 1->2->3
Output: 124 
Your Task:
Your task is to complete the function addOne() which takes the head of the linked list as the only argument and returns the head of the modified linked list. The driver code prints the number.
Note: The head represents the left-most digit of the number.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
"""
'''

class Node:
    def __init__(self, data):   # data -> dataue stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev

        carry = 1
        prev = None
        curr = head
        while curr:
            # Add 1 to the current node's dataue along with carry
            curr.data += carry
            carry = curr.data // 10
            curr.data %= 10
            prev = curr
            curr = curr.next
        
        # If carry is left after traversing all nodes
        if carry:
            prev.next = Node(carry)

        # Reverse the linked list back
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev

        return head
