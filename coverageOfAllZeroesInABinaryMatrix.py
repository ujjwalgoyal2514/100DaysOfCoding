"""Given a binary matrix having n rows and m columns, your task is to find the sum of coverage of all zeros in the matrix where coverage for a particular 0 is defined as a total number of ones around a zero in left, right, up, and bottom directions.
 

Examples:

Input: 
matrix = [[0, 1, 0],
          [0, 1, 1], 
          [0, 0, 0]]
Output: 6
Input: 
matrix = [[0, 1]]
Output: 1
Expected Time Complexity: O(n * m)
Expected Space Complexity: O(1)
 

Constraints:
1 <= mat.size, mat[0].size <= 100"""
class Solution:
	def FindCoverage(self, matrix):
	    row, col = len(matrix), len(matrix[0])
	    count = 0
	    
	    for i in range(row):
	        for j in range(col):
	            if matrix[i][j]==0:
	                if -1<i-1<row and matrix[i-1][j]==1:
	                    count+=1
	                if -1<j-1<col and matrix[i][j-1]==1:
	                    count+=1
	                if -1<j+1<col and matrix[i][j+1]==1:
	                    count+=1
	                if -1<i+1<row and matrix[i+1][j]==1:
	                    count+=1
	    return count