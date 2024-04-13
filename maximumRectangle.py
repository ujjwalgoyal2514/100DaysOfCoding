"""Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        ans = 0
        dp = {}

        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='0':
                    dp[(i,j)]=(0,0)
                else:
                    x = dp[(i,j-1)][0]+1 if j>0 else 1
                    y = dp[(i-1,j)][1]+1 if i>0 else 1
                    dp[(i,j)] = (x,y)
                    ans = max(x,y,ans)
                    minWidth = x
                    # verical max possible
                    for r in range(i-1,i-y,-1):
                        minWidth = min(minWidth,dp[(r,j)][0])
                        ans = max(ans,minWidth*(i-r+1))
        
        
        return ans