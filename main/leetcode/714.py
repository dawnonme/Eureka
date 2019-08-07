class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        have, not_have = -prices[0], 0
        for i in range(1, len(prices)):
            not_have = max(not_have, have + prices[i] - fee)
            have = max(have, not_have - prices[i])
        return not_have

    def max_profit(self, prices, fee):
        if len(prices) < 2:
            return 0
        profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] > min_price + fee:
                profit += prices[i] - min_price - fee
                min_price = prices[i] - fee
        return profit