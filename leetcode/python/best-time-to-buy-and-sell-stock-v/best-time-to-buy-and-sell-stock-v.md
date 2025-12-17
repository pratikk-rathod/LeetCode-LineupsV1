

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Intuition</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-17T18:20:13.126Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3573. Best Time to Buy and Sell Stock VSolvedMediumTopicsCompaniesHintYou are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.

You are allowed to make at most k transactions, where each transaction can be either of the following:


	
	Normal transaction: Buy on day i, then sell on a later day j where i < j. You profit prices[j] - prices[i].
	
	
	Short selling transaction: Sell on day i, then buy back on a later day j where i < j. You profit prices[i] - prices[j].
	


Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day you are selling or buying back as part of a previous transaction.

Return the maximum total profit you can earn by making at most k transactions.

 
Example 1:


Input: prices = [1,7,9,8,2], k = 2

Output: 14

Explanation:
We can make $14 of profit through 2 transactions:


	A normal transaction: buy the stock on day 0 for $1 then sell it on day 2 for $9.
	A short selling transaction: sell the stock on day 3 for $8 then buy back on day 4 for $2.



Example 2:


Input: prices = [12,16,19,19,8,1,19,13,9], k = 3

Output: 36

Explanation:
We can make $36 of profit through 3 transactions:


	A normal transaction: buy the stock on day 0 for $12 then sell it on day 2 for $19.
	A short selling transaction: sell the stock on day 3 for $19 then buy back on day 4 for $8.
	A normal transaction: buy the stock on day 5 for $1 then sell it on day 6 for $19.



 
Constraints:


	2 <= prices.length <= 103
	1 <= prices[i] <= 109
	1 <= k <= prices.length / 2

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Data:
    def __init__(self, profit, buy, sell):
        self.profit=profit
        self.buy=buy
        self.sell=sell
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        x0=prices[0]
        dp=[Data(0, -x0, x0) for _ in range(k+1)]
        n=len(prices)
        for i in range(1, n):
            x=prices[i]
            for t in range(k, 0, -1):
                cur=dp[t]
                prevP=dp[t-1].profit
                # close transaction t
                cur.profit=max(cur.profit, cur.buy+x, cur.sell-x)
                # open transaction t
                cur.buy=max(cur.buy,  prevP-x)
                cur.sell=max(cur.sell, prevP+x)
        return dp[-1].profit
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

