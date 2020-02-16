# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxProfit(self, prices):
        ''''''
        if prices == []:
            return 0

        min_price = prices[0]       # 当前最低价格
        max_profit = 0              # 当前最高利润
        for i, price in enumerate(prices):
            min_price = min(price, min_price)   # 当前最低价格 为当前价格 和 之前的最低价格 中的更小的
            max_profit = max(price-min_price, max_profit)       # 最大利润，为当前最大利润 和 之前最大利润的更大
        return max_profit

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices))