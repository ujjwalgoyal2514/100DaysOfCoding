"""Given a square matrix[][] of size N x N. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space.

Example 1:

Input:
N = 3
matrix[][] = [[1 2 3],
              [4 5 6],
              [7 8 9]]
Output:
3 6 9 
2 5 8 
1 4 7
Your Task:
You only need to implement the given function rotate(). Do not read input, instead use the arguments given in the function. 

Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 50
1 <= matrix[][] <= 100

"""
def rotate(matrix): 
    #code here
    n=len(matrix)
    ans=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[n-j-1][i]=matrix[i][j]
    for i in range(n):
        for j in range(n):
            matrix[i][j]=ans[i][j]
    return matrix