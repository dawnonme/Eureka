class Solution:
    def max_profit_309(self, prices: List[int]) -> int:
        ''' 309: Best Time to Buy and Sell Stock with Cooldown '''
        if not prices:
            return 0
        N = len(prices)

        buy, sell, cool = [0] * N, [0] * N, [0] * N

        # buying stock at day 0 will cost prices[0]
        buy[0] = -prices[0]

        for i in range(1, N):
            # choose to buy on day i - 1 or cool down on i - 1 and buy on day i
            buy[i] = max(buy[i-1], cool[i-1] - prices[i])

            # choose to do nothing on day i - 1 or sell on day i
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])

            # choose to cool down on day i - 1 or sell on day i - 1
            cool[i] = max(cool[i-1], sell[i-1])

        return sell[-1]
