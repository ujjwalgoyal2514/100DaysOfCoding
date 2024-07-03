"""Given a sorted linked list, delete all nodes that have duplicate numbers (all occurrences), leaving only numbers that appear once in the original list, and return the head of the modified linked list. 

Examples:

Input: Linked List = 23->28->28->35->49->49->53->53
Output: 23 35
Explanation: 

The duplicate numbers are 28, 49 and 53 which are removed from the list.
Input: Linked List = 11->11->11->11->75->75
Output: Empty list
Explanation: 

All the nodes in the linked list have duplicates. Hence the resultant list would be empty.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ size(list) ≤ 105
"""
"""
# Linked list Node class

    class Node :
        def __init__(self, val):
            self.data = val
            self.next = None

"""
from collections import OrderedDict

class Solution:
    
    # Finding the unique element while maintaning the sequence 
    def findUniqueElements(self, arr):
        count_dict = OrderedDict()
        
        # Count occurrences of each element
        for num in arr:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        
        # Collect elements that appear exactly once, maintaining order
        unique_elements = [num for num, count in count_dict.items() if count == 1]
        
        return unique_elements
    
    
    def removeAllDuplicates(self, head):
        #code here
        arr=[]
        temp = head 
        while temp:
            arr.append(temp.data)
            temp =temp.next 
            
        ans =[]
        ans =self.findUniqueElements(arr)
            
            
        temp = head 
        i = 0
        while  temp and i < len(ans):
            temp.data = ans[i]
            i+=1 
            if  i  == len(ans):temp.next = None 
            else : temp = temp.next
              
        return head