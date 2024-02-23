"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new=ListNode(-1,None)
        ans=new
        c=0
        itr=head
        while(itr):
            itr=itr.next
            c+=1
        print(c)
        c=c//2
        print(c)
        it=head
        index=0
        while(it):
            if index==c:
                while(it):
                    ans.next=ListNode(it.val,None)
                    ans=ans.next
                    it=it.next
            else:
                index+=1
                it=it.next
        return new.next