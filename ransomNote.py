"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count={}
        for j in magazine:
            if j in count:
                count[j]+=1
            else:
                count[j]=1
        for i in ransomNote:
            if i in count and count[i]>0:
                count[i]-=1
            else:
                return False
        return True