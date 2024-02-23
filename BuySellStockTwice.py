"""
In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, the second transaction can only start after the first one is complete (buy->sell->buy->sell). The stock prices throughout the day are represented in the form of an array of prices. 

Given an array price of size n, find out the maximum profit that a share trader could have made.

Example 1:

Input:
n = 6
prices[] = {10,22,5,75,65,80}
Output:
87
Explanation:
Trader earns 87 as sum of 12, 75 Buy at 10, sell at 22, Buy at 5 and sell at 80.
Example 2:

Input:
n = 7
prices[] = {2,30,15,10,8,25,80}
Output:
100
Explanation:
Trader earns 100 as sum of 28 and 72 Buy at price 2, sell at 30, Buy at 8 and sell at 80,
Your Task:

Complete the function maxProfit() which takes an integer array price as the only argument and returns an integer, representing the maximum profit, if only two transactions are allowed.


"""
from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:
        # code here
        arr=[0]*(n)
        maxi = price[-1]
        ans = 0 
        for i in range(n-1, -1 , -1):
            if price[i] >  maxi : 
                maxi = price[i]
                
            else : 
                ans= max(ans,maxi- price[i])
                arr[i]= ans 
              
        mini = price[0]
        ansi = 0 
        num=[0]*n
        for i in range(n):
            if price[i] < mini : 
                mini = price[i]
            else : 
                ansi = max(price[i]- mini, ansi )
                num[i]= ansi
            
        #print(arr, num)
        fans = max(num[-1], arr[0])
        for i in range(n-1):
            fans = max(fans , num[i]+ arr[i+1])
            
        return  fans

