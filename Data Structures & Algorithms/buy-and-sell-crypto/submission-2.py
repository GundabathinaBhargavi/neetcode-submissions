class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr=[0]
        
        for i in range(len(prices)-1):
            diff=0
            for j in range(i+1,len(prices)):
                diff=max(diff,prices[j]-prices[i])
            arr.append(diff)
        return max(arr)