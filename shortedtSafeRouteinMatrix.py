"""
Given a matrix mat[][] with r rows and c columns, where some cells are landmines (marked as 0) and others are safe to traverse. Your task is to find the shortest safe route from any cell in the leftmost column to any cell in the rightmost column of the mat. You cannot move diagonally, and you must avoid both the landmines and their adjacent cells (up, down, left, right), as they are also unsafe.

Example 1:

Input:
mat = [1, 0, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 1, 1],
      [1, 1, 1, 0, 1],
      [1, 1, 1, 1, 0]
Output: 
6
Explanation: 
We can see that length of shortest
safe route is 6 (Highlighted in Bold).
[1 0 1 1 1]
[1 1 1 1 1] 
[1 1 1 1 1]
[1 1 1 0 1] 
[1 1 1 1 0]
Example 2:

Input:
mat = [1, 1, 1, 1, 1],
      [1, 1, 0, 1, 1],
      [1, 1, 1, 1, 1]
Output: 
-1
Explanation: There is no possible path from
first column to last column.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findShortestPath() which takes matrix as input parameter and return an integer denoting the shortest safe path form any cell in leftmost column to any cell in rightmost column of mat. If there is no possible path, return -1. 

Expected Time Complexity: O(r * c)
Expected Auxiliary Space: O(1)

Constraints:
1 <= r, c <= 103
0 <= mat[][] <= 1
"""
from typing import List
from collections import deque

class Solution:
    def findShortestPath(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return -1
        
        n, m = len(mat), len(mat[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  
        def is_blocked(x, y):
            if mat[x][y] == 0:
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == 0:
                    return True
            return False
        
        queue = deque([(i, 0, 1) for i in range(n) if not is_blocked(i, 0)])
        vis = [[False for _ in range(m)] for _ in range(n)]  # Visited matrix
        
        while queue:
            x, y, dist = queue.popleft()
            if y == m - 1:
                return dist
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and not is_blocked(nx, ny):
                    vis[nx][ny] = True  
                    queue.append((nx, ny, dist + 1))
        
        return -1