"""Rohan has a special love for the matrices especially for the first element of the matrix. Being good at Mathematics, he also loves to solve the different problem on the matrices. So one day he started to multiply the matrix with the original matrix.  The elements of the original matrix a are given by [a00=1 , a01=1, a10=1, a11=0].
Given the power of the matrix, n calculate the an and return the a10 element mod 1000000007.

Example 1:

Input: 
n = 3
Output: 
2 
Explanation: Take the cube of the original matrix 
i.e a3 and the (a10)th element is 2.
Example 2:

Input: 
n = 4
Output: 
3
Explanation: Take the cube of the original matrix 
i.e a4 and the (a10)th element is 3.
Your Task:  
You dont need to read input or print anything. Complete the function firstElement() which takes n as input parameter and returns the a10 element mod 1000000007 of an.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1<= n <=106

"""
import numpy as np
class Solution:
    def firstElement (self, n):
        MODULO = 10**9 + 7
        
        arr = np.array([[1, 1], [1, 0]], dtype=int)
        res = np.identity(2, dtype=int)
        while n:
            if n & 1:
                res = np.matmul(res, arr) % MODULO
            arr = np.matmul(arr, arr) % MODULO
            n >>= 1
        return res[1, 0]