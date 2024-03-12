"""Consider the generalized Fibonacci number g, which is dependent on a, b and c as follows :-
g(1) = 1, g(2) = 1. For any other number n, g(n) = a*g(n-1) + b*g(n-2) + c.

For a given value of m, determine g(n)%m.

Example 1:

Input:
a = 3
b = 3
c = 3
n = 3
m = 5
Output:
4
Explanation:
g(1) = 1 and g(2) = 1 
g(3) = 3*g(2) + 3*g(1) + 3 = 3*1 + 3*1 + 3 = 9
We need to return answer modulo 5, so 9%5 = 4, is the answer.
Example 2:

Input:
a = 2
b = 2
c = 2
n = 4
m = 100
Output:
16
Explanation:
g(1) = 1 and g(2) = 1
g(3) = 2*g(2) + 2*g(1) + 2 = 2*1 + 2*1 + 2 = 6
g(4) = 2*g(3) + 2*g(2) + 2  = 2*6 + 2*1 + 2 = 16
We need to return answer modulo 100, so 16%100 = 16, is the answer.
"""
class Solution:
    def mul(self, res, mat,m):
        temp_res=[[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    temp_res[i][j]+=res[i][k]*mat[k][j]
                    temp_res[i][j]%=m
        for i in range(3):
            for j in range(3):
                res[i][j]=temp_res[i][j]
    def exp(self, n, m):
        while n>0:
            if n & 1:
                self.mul(self.res,self.mat,m)
            self.mul(self.mat,self.mat,m)
            n//=2
    def genFibNum(self, a, b, c, n, m):
        # code here 
        if n<=2:
            return 1%m
        self.mat=[[0]*3 for _ in range(3)]
        self.mat[0][0]=a
        self.mat[0][1]=b
        self.mat[0][2]=self.mat[1][0]=self.mat[2][2]=1
        self.res=[[0]*3 for _ in range(3)]
        self.res[0][0]=self.res[1][1]=self.res[2][2]=1
        
        self.exp(n-2,m)
        
        return (self.res[0][0]+self.res[0][1]+c*self.res[0][2])%m

