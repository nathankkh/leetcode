class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        cheapest = 10 * (10**4)
        profit = -1
        for price in prices:
            if price < cheapest:
                cheapest = price
            else:
                if price - cheapest > profit:
                    profit = price - cheapest
        if profit < 0:
            return 0
        else:
            return profit


"""
Restrictions: Can only look forward

Edge case:
- len(prices) = 1
    -> 
- prices are descending order (early termination)

Brute force: for each item, loop through remaining 

---
Store cheapest price variable
Store greatest profit
Store (buy_date, sell_date)

Outer for:
Is this cheaper than my cheapest? If so, update cheapest and continue
Else, is curr - cheapest greater than my greatest profit so far? If yes, update else continue

"""
