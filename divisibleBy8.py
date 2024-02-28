"""Given a string representation of a decimal number s, check whether it is divisible by 8.

Example 1:

Input:
s = "16"
Output:
1
Explanation:
The given number is divisible by 8,
so the driver code prints 1 as the output.
Example 2:

Input:
s = "54141111648421214584416464555"
Output:
-1
Explanation:
Given Number is not divisible by 8, 
so the driver code prints -1 as the output.

"""

class Solution:
    def DivisibleByEight(self,s):
        #code here
        if len(s)<3:
            return 1 if int(s)//8 else 0
        if int(s[-3:])%8==0 or s[-3:]=="000":
            return 1
        else:
            return -1