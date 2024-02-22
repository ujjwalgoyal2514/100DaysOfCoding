"""
Given two strings s and t of length n and m respectively. Find the count of distinct occurrences of t in s as a sub-sequence modulo 109 + 7.

Example 1:

Input:
s = "banana" , t = "ban"
Output: 
3
Explanation: 
There are 3 sub-sequences:[ban], [ba n], [b an].
Example 2:

Input:
s = "geeksforgeeks" , t = "ge"
Output: 
6
Explanation: 
There are 6 sub-sequences:[ge], [ge], [g e], [g e] [g e] and [g e].
Your Task:
You don't need to read input or print anything.Your task is to complete the function subsequenceCount() which takes two strings as argument s and t and returns the count of the sub-sequences modulo 109 + 7.

Expected Time Complexity: O(n*m).
Expected Auxiliary Space: O(n*m).

"""
class Solution:
    def sequenceCount(self,s, t):
        m=10**9+7
        def calc(ind1,ind2):
            if ind2>=len(t):
                return 1
            if ind1>=len(s):
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]%m
            npi=0+calc(ind1+1,ind2)
            pi=0
            if s[ind1]==t[ind2]:
                pi=0+calc(ind1+1,ind2+1)
                
            dp[ind1][ind2]=(pi+npi)%m
            return dp[ind1][ind2]%m
        
        dp=[[-1 for i in range(len(t))] for j in range(len(s))]
        return calc(0,0)