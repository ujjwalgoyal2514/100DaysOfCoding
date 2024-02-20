"""
Your laptop keyboard is faulty, and whenever you type a character 'i' on it, it reverses the string that you have written. Typing other characters works as expected.

You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.

Return the final string that will be present on your laptop screen.
"""
class Solution:
    def finalString(self, s: str) -> str:
        while "i" in s:
            index=s.index("i")

            #first half and second half
            first=s[:index][::-1]
            print(first)
            second=s[index+1:]

            s="".join([first,second])
        return s