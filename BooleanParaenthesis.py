"""
Given a boolean expression s of length n with following symbols.
Symbols
    'T' ---> true
    'F' ---> false
and following operators filled between symbols
Operators
    &   ---> boolean AND
    |   ---> boolean OR
    ^   ---> boolean XOR
Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

Note: The answer can be large, so return it with modulo 1003

Example 1:

Input: 
n = 7
s = T|T&F^T
Output: 
4
Explaination: 
The expression evaluates to true in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and (T|((T&F)^T)).
Example 2:

Input: 
n = 5
s = T^F|F
Output: 
2
Explaination: 
((T^F)|F) and (T^(F|F)) are the only ways.

"""

class Solution:
    def countWays(self, n, s):
        # code here
        dpTrue=[[0]*n for _ in range(n)]
        dpFalse=[[0]*n for _ in range(n)]
        
        mod=1003
        
        for i in range(0,n,2):
            if s[i]=="T":
                dpTrue[i][i]=1
                dpFalse[i][i]=0
            else:
                dpTrue[i][i]=0
                dpFalse[i][i]=1
        
        x=2
        while x<N:
            for i in range(0,n-x+1,2):
                for j in range(i+1,i+x,2):
                    if s[j]=="&":
                        dpTrue[i][i+x]+=dpTrue[i][j-1]*dpTrue[j+1][i+x]
                        dpFalse[i][i+x]+=dpFalse[i][j-1]*dpFalse[j+1][i+x]+dpFalse[i][j-1]*dpTrue[j+1][i+x]+dpTrue[i][j-1]*dpFalse[j+1][i+x]
                    elif s[j]=="|":
                        dpTrue[i][i+x]+=dpTrue[i][j-1]*dpTrue[j+1][i+x]+dpFalse[i][j-1]*dpTrue[j+1][i+x]+dpTrue[i][j-1]*dpFalse[j+1][i+x]
                        dpFalse[i][i+x]+=dpFalse[i][j-1]*dpFalse[j+1][i+x]
                    else:
                        dpTrue[i][i+x]+=dpTrue[i][j-1]*dpFalse[j+1][i+x]+dpFalse[i][j-1]*dpTrue[j+1][i+x]
                        dpFalse[i][i+x]+=dpTrue[i][j-1]*dpTrue[j+1][i+x]+dpFalse[i][j-1]*dpFalse[j+1][i+x]
                    dpTrue[i][i+x]=dpTrue[i][i+x]%mod
                    dpFalse[i][i+x]%=mod
            x+=2
        return dpTrue[0][n-1]%mod