def matrix(prices):
    buy=0
    sell=1
    max_profit=0
    i=0
    j=0
    while(sell<len(prices)):
        profit=prices[sell]-prices[buy]
        if prices[buy]<prices[sell]:
            max_profit=max(profit,max_profit)
        else:
            buy=sell
        sell+=1
    return max_profit ,buy,sell   

print(matrix([7,5,3,6,1]))