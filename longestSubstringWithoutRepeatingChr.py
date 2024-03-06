""""Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        i=0
        j=0
        maxi=0
        while j<len(s):
            if s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
            if len(d)== j-i+1:
                maxi=max(maxi,j-i+1)
                j+=1
            elif len(d)<j-i+1:
                while len(d)<j-i+1:
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                    i+=1
                j+=1
        return maxi