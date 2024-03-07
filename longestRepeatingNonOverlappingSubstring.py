""" Given a string s of length n, find the longest repeating non-overlapping substring in it. In other words find 2 identical substrings of maximum length which do not overlap. Return the longest non-overlapping substring. Return "-1" if no such string exists.

Note: Multiple Answers are possible but you have to return the substring whose first occurrence is earlier.

For Example: "abhihiab", here both "ab" and "hi" are possible answers. But you will have to return "ab" because it's first occurrence appears before the first occurrence of "hi".

Example 1:

Input:
n = 9
s = "acdcdacdc"
Output:
"acdc"
Explanation:
The string "acdc" is the longest Substring of s which is repeating but not overlapping.
Example 2:

Input:
n = 7
s = "heheheh"
Output:
"heh"
Explanation:
The string "heh" is the longest Substring of s which is repeating but not overlapping.
Your Task:
You don't need to read input or print anything. Your task is to complete the function longestSubstring() which takes an Integer n and a string s as input and returns the answer.
"""
class Solution:
    def longestSubstring(self, s , n):
        # code here 
        max_len=0
        end=-1
        dp=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(i+1,n):
                if s[i]==s[j] and j-i>dp[i][j]:
                    dp[i+1][j+1]=1+dp[i][j]
                    if dp[i+1][j+1]>max_len:
                        max_len=dp[i+1][j+1]
                        end=i
        if end==-1:
            return "-1"
        return s[end-max_len+1:end+1]