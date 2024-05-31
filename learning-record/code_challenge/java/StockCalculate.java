package java;

/**
 * You are given an array prices where prices[i] is the price of a given stock on the ith day.
 * <p>
 * You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
 * <p>
 * Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 * <p>
 * Example 1:
 * <p>
 * Input: prices = [7,1,5,3,6,4]
 * Output: 5
 * <p>
 * Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
 * Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
 * <p>
 * Example 2:
 * <p>
 * Input: prices = [7,6,4,3,1]
 * Output: 0
 * Explanation: In this case, no transactions are done and the max profit = 0.
 * <p>
 * Constraints:
 * <p>
 * 1 <= prices.length <= 105
 * 0 <= prices[i] <= 104
 */
public class StockCalculate {
    public static void main(String[] args) {
        int prices[] = {7, 10, 2, 3, 4, 1, 5, 3, 6, 4, 9, 8, 7, 2, 3, 4, 5, 12};
        int maxProfit = maxProfit(prices);
        System.out.println("maxProfit:" + maxProfit);
    }

    private static int maxProfit(int prices[]) {
        int maxProfit = 0;
        if (prices.length > 100000) {
            return maxProfit;
        }
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i] < 0 || prices[i] > 10000) {
                return maxProfit;
            }
        }
        if (prices.length >= 1 && prices.length <= 100000) {
            int buy = prices[0];
            for (int i = 1; i < prices.length; i++) {
                int sell = prices[i];
                if (sell > buy) {
                    int profit = sell - buy;
                    if (profit > 0 && maxProfit <= profit) {
                        maxProfit = profit;
                    }
                } else {
                    buy = sell;
                }
            }
        }
        return maxProfit;
    }
}
