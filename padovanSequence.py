"""Given a number n, find the nth number in the Padovan Sequence.

A Padovan Sequence is a sequence which is represented by the following recurrence relation
P(n) = P(n-2) + P(n-3)
P(0) = P(1) = P(2) = 1

Note: Since the output may be too large, compute the answer modulo 10^9+7.

Examples :

Input: n = 3
Output: 2
Explanation: We already know, P1 + P0 = P3 and P1 = 1 and P0 = 1
Input: n = 4
Output: 2
Explanation: We already know, P4  = P2 + P1 and P2 = 1 and P1 = 1
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 106

"""
class Solution:
    def padovanSequence(self, n):
        
        step1,step2,step3 = 1,1,1
        
        if n == 1 or n == 2: return 1
        
        for i in range(3,n):
            temp = (step1 + step2) % 1000000007
            step1,step2,step3 = step2,step3,temp
            
            
        return (step1+step2)% 1000000007