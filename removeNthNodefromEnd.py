"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        itr=head
        c=0
        while itr:
            c+=1
            itr=itr.next
        print(c)
        if c==n:
            return head.next
        element=c-n
        print(element)
        index=0
        itr=head
        while itr:
            if index==element-1:
                itr.next=itr.next.next
            index+=1
            itr=itr.next
        return head