"""Given a singly linked list having n nodes containing english alphabets ('a'-'z'). Rearrange the linked list in such a way that all the vowels come before the consonants while maintaining the order of their arrival. 

Example 1:

Input:
n = 9
linked list: a -> b -> c -> d -> e -> f -> g -> h -> i 
Output: 
a -> e -> i -> b -> c -> d -> f -> g -> h
Explanation: 
After rearranging the input linked list according to the condition the resultant linked list will be as shown in output.
Example 2:

Input:
n = 8
linked list: a -> b -> a -> b -> d -> e -> e -> d 
Output: 
a -> a -> e -> e -> b -> b -> d -> d
Explanation: 
After rearranging the input linked list according to the condition the resultant linked list will be as shown in output.
Your Task:
Your task is to complete the function arrangeCV(), which takes head of linked list and arranges the list in such a way that all the vowels come before the consonants while maintaining the order of their arrival and returns the head of the updated linked list.

Expected Time Complexity :  O(n)
Expected Auxiliary Space :  O(1)

Constraints:
1 <= n <= 104
'a' <= elements of linked list <= 'z'"""
class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        vow=['a','e','i','o','u']
        v=[]
        c=[]
        while head:
            if head.data in vow:
                v.append(head.data)
            else:
                c.append(head.data)
            head=head.next
        if len(v)>0:
            k=Node(v[0])
            head=k
            for i in v[1:]:
                k.next=Node(i)
                k=k.next
            for i in c:
                k.next=Node(i)
                k=k.next
        elif len(c)>0:
            k=Node(c[0])
            head=k
            for i in c[1:]:
                k.next=Node(i)
                k=k.next
            
            
        return head
