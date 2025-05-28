# Problem 1: Stock Buy and Sell – Max one Transaction Allowed
class StockSolution:
    def maximumProfit(self, prices):
        buy_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - buy_price)
            buy_price = min(buy_price, prices[i])
        return max_profit


# Problem 2: Minimize the Heights II
class HeightSolution:
    def getMinDiff(self, arr, k):
        arr.sort()
        n = len(arr)
        ans = arr[-1] - arr[0]
        for i in range(1, n):
            if arr[i] - k < 0:
                continue
            mn = min(arr[0] + k, arr[i] - k)
            mx = max(arr[i - 1] + k, arr[-1] - k)
            ans = min(ans, mx - mn)
        return ans


# Example usage
if __name__ == "_main_":
    # Stock Buy and Sell
    stock = StockSolution()
    print(stock.maximumProfit([7, 10, 1, 3, 6, 9, 2]))  # Output: 8
    print(stock.maximumProfit([7, 6, 4, 3, 1]))         # Output: 0
    print(stock.maximumProfit([1, 3, 6, 9, 11]))        # Output: 10

    # Minimize Heights II
    height = HeightSolution()
    print(height.getMinDiff([1, 5, 8, 10], 2))          # Output: 5
    print(height.getMinDiff([3, 9, 12, 16, 20], 3))     # Output: 11