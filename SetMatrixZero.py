
# Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

# ***************************************BRUTE FORCE************************************
def row(i,a):
    for j in range(len(a[0])):
        if a[i][j]!=0:
            a[i][j]=-1
def col(j,a):
    for i in range(len(a)):
        if a[i][j]!=0:
            a[i][j]=-1             
def matrix(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==0:
                row(i,a)
                col(j,a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==-1:
                a[i][j]=0
    return a


print(matrix([[1,1,1],[1,0,1],[1,1,1]]))   