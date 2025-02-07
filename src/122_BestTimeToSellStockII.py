class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices) - 1):
            curr = prices[i]
            next_p = prices[i+1]
            if curr < next_p:
                profit += next_p - curr
        return profit


"""
Restrictions: Can only look forward
Greedy algo

Keep taking profit

4,1,7,2,5,1

6 + 3

1,2,4,6,3

7,6,5,4,9
"""
