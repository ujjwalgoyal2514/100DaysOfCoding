"""You are given an integer k and matrix mat. Rotate the elements of the given matrix to the left k times and return the resulting matrix.

Examples:

Input: k=1, mat=[[1,2,3],[4,5,6],[7,8,9]]
Output:
2 3 1
5 6 4
8 9 7
Explanation: Rotate the matrix by one
1 2 3       2 3 1
4 5 6  =>  5 6 4
7 8 9       8 9 7
Input: k=2, mat=[[1,2,3],[4,5,6],[7,8,9]]
Output:
3 1 2
6 4 5
9 7 8
Explanation: After rotating the matrix looks like
1 2 3       2 3 1       3 1 2
4 5 6  =>  5 6 4  =>   6 4 5
7 8 9       8 9 7       9 7 8
Expected Time Complexity: O(n*m)
Expected Auxillary Space: O(n*m)

Constraints:
1<= mat.size, mat[0].size, mat[i][j] <=1000
1<=k<=10000"""
class Solution:
    def reverse(self,arr,s,e):
        while s<e:
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1

    def rotateMatrix(self, k, mat):
        r,c=len(mat),len(mat[0])
        k=k%c
        for i in range(r):
            self.reverse(mat[i],0,k-1)
            self.reverse(mat[i],k,c-1)
            self.reverse(mat[i],0,c-1)
        return mat