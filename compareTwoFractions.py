"""You are given a string str containing two fractions a/b and c/d, compare them and return the greater. If they are equal, then return "equal".

Note: The string str contains "a/b, c/d"(fractions are separated by comma(,) & space( )). 

Examples

Input: str = "5/6, 11/45"
Output: 5/6
Explanation: 5/6=0.8333 and 11/45=0.2444, So 5/6 is greater fraction.
Input: str = "8/1, 8/1"
Output: equal
Explanation: We can see that both the fractions are same, so we'll return a string "equal".
Input: str = "10/17, 9/10"
Output: 9/10
Explanation: 10/17 = 0.588 & 9/10 = 0.9, so the greater fraction is "9/10".
Expected Time Complexity: O(len|str|)
Expected Auxiliary Space: O(1)

Constraints:
0<=a,c<=103
1<=b,d<=103"""
class Solution:
    def compareFrac (self, str):
        
        # code here
        a=''
        b=''
        c=''
        d=''
        i=0
        while(str[i]!=','):
            a+=str[i]
            i+=1 
        i+=2
        b=str[i:]
        l=a.split('/')
        l2=b.split('/')
        n1=int(l[0])
        n2=int(l2[0])
        d1=int(l[1])
        d2=int(l2[1])
                
        if n1/d1==n2/d2:
            return "equal"
        elif n1/d1>n2/d2:
            return a
        else:
            return b