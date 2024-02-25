"""Given two linked lists sorted in increasing order, create a new linked list representing the intersection of the two linked lists. The new linked list should be made with without changing the original lists.

Note: The elements of the linked list are not necessarily distinct.

Example 1:

Input:
LinkedList1 = 1->2->3->4->6
LinkedList2 = 2->4->6->8
Output: 2 4 6
Explanation: For the given two
linked list, 2, 4 and 6 are the elements
in the intersection.
Example 2:

Input:
LinkedList1 = 10->20->40->50
LinkedList2 = 15->40
Output: 40
Your Task:
You don't have to take any input of print anything. Your task is to complete the function findIntersection(), which will take head of both of the linked lists as input and should find the intersection of two linked list and add all the elements in intersection to the third linked list and return the head of the third linked list.

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(n+m)
Note: n, m are the size of the respective linked lists.
"""

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self,head1,head2):
        #return head
        d={}
        itr=head1
        while itr:
            d[itr.data]=d.get(itr.data,0)+1
            itr=itr.next
        head=None
        tail=None
        itr=head2
        while itr:
            if itr.data in d and d[itr.data]:
                if head==None:
                    head=Node(itr.data)
                    tail=head
                else:
                    tail.next=Node(itr.data)
                    tail=tail.next
                d[itr.data]-=1
            itr=itr.next
        return head