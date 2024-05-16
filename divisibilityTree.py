"""Given a tree with n nodes where n is even. The tree is numbered from 1 to n, has n - 1 edges and is rooted at node 1. Your task is to eliminate the maximum number of edges resulting in a set of disjoint trees where the number of nodes in each tree is divisible by 2.

Example 1:

Input: 
n = 10
edges = {{2,1},{3,1},{4,3},{5,2},{6,1},{7,2},{8,6},{9,8},{10,8}}
Output:
2
Explanation:
Original tree:

   
After removing edge 1-3 and 1-6, each remaining component consists of even number of nodes. 


Example 2:

Input: 
n = 4
edges = {{2,1},{4,2},{1,3}}
Output:
1
Explanation:
After removing 2-1, each remaining component consists of even number of nodes. 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function minimumEdgeRemove() which takes n and edges as input parameters and returns the maximum number of edges that need to be removed from the given tree.

Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:
1 <= n <= 105
edges.length == n - 1
1 <= edges[i][0], edges[i][1] <= n
"""
from typing import List


class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        # code here
        counts = [0]*(n+1)
        graph = [[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node,prev,counts,graph):
            size = 1
            for neigh in graph[node]:
                if neigh == prev:
                    continue
                size += dfs(neigh,node,counts,graph)
            
            counts[node] = size
            return size
        
        dfs(1,-1,counts,graph)
        ans = 0
        for i in range(2,n+1):
            if counts[i] % 2 == 0:
                ans += 1
                
        return ans