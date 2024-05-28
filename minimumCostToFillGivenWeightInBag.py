"""Given an array cost[] of positive integers of size n and an integer w, where cost[i] represents the cost of an i kg packet of oranges, the task is to find the minimum cost to buy exactly w kg of oranges. The cost array has a 1-based indexing. If buying exactly w kg of oranges is impossible, then return -1.
Note:
1. cost[i] = -1 means that i kg packet of orange is unavailable.
2. It may be assumed that there is an infinite supply of all available packet types.

Example 1:

Input: 
n = 5
cost[] = {20, 10, 4, 50, 100} 
w = 5
Output: 
14
Explanation: 
Purchase the 2kg packet for 10 coins and the 3kg packet for 4 coins to buy 5kg of oranges for 14 coins.
Example 2:

Input: 
n = 5
cost[] = {-1, -1, 4, 3, -1}
w = 5
Output: 
-1
Explanation: 
It is not possible to buy 5 kgs of oranges.
Your Task:  
You don't need to read input or print anything. Complete the function minimumCost() which takes integers n and w, and integer array cost[] as input parameters and returns the minimum cost to buy exactly w kg of oranges, If buying exactly w kg of oranges is impossible, then return -1.

Expected Time Complexity: O(n*w)
Expected Auxiliary Space: O(n*w)

Constraints:
1 ≤ n, w ≤ 2*102
1 ≤ cost[i] ≤ 105
cost[i] ≠ 0"""

from typing import List


class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        from sys import setrecursionlimit
        setrecursionlimit(2*10**3)
        from functools import lru_cache
        @lru_cache(None)
        def dfs(ix=n-1,wth=w):
            nonlocal cost
            if wth==0:
                return 0
            if ix<0:
                return float('inf')
            if cost[ix]==-1:
                return dfs(ix-1,wth)
            mn=dfs(ix-1,wth)
            if wth-ix-1>=0:
                mn=min(
                    mn,
                    dfs(ix,wth-ix-1)+cost[ix],
                    dfs(ix-1,wth-ix-1)+cost[ix]
                    )
            return mn
        mn=dfs()
        return mn if mn!=float('inf') else -1