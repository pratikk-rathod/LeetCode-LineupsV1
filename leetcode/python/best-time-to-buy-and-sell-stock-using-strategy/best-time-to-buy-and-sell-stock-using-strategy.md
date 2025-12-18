

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Intuition</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/submissions/1859190897/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-18T18:22:42.325Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3652. Best Time to Buy and Sell Stock using StrategySolvedMediumTopicsCompaniesHintYou are given two integer arrays prices and strategy, where:


	prices[i] is the price of a given stock on the ith day.
	strategy[i] represents a trading action on the ith day, where:
	
		-1 indicates buying one unit of the stock.
		0 indicates holding the stock.
		1 indicates selling one unit of the stock.
	
	


You are also given an even integer k, and may perform at most one modification to strategy. A modification consists of:


	Selecting exactly k consecutive elements in strategy.
	Set the first k / 2 elements to 0 (hold).
	Set the last k / 2 elements to 1 (sell).


The profit is defined as the sum of strategy[i] * prices[i] across all days.

Return the maximum possible profit you can achieve.

Note: There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.

 
Example 1:


Input: prices = [4,2,8], strategy = [-1,0,1], k = 2

Output: 10

Explanation:

ModificationStrategyProfit CalculationProfitOriginal[-1, 0, 1](-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 84Modify [0, 1][0, 1, 1](0 × 4) + (1 × 2) + (1 × 8) = 0 + 2 + 810Modify [1, 2][-1, 0, 1](-1 × 4) + (0 × 2) + (1 × 8) = -4 + 0 + 84

Thus, the maximum possible profit is 10, which is achieved by modifying the subarray [0, 1]​​​​​​​.


Example 2:


Input: prices = [5,4,3], strategy = [1,1,0], k = 2

Output: 9

Explanation:


ModificationStrategyProfit CalculationProfitOriginal[1, 1, 0](1 × 5) + (1 × 4) + (0 × 3) = 5 + 4 + 09Modify [0, 1][0, 1, 0](0 × 5) + (1 × 4) + (0 × 3) = 0 + 4 + 04Modify [1, 2][1, 0, 1](1 × 5) + (0 × 4) + (1 × 3) = 5 + 0 + 38

Thus, the maximum possible profit is 9, which is achieved without any modification.



 
Constraints:


	2 <= prices.length == strategy.length <= 105
	1 <= prices[i] <= 105
	-1 <= strategy[i] <= 1
	2 <= k <= prices.length
	k is even

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n, k2=len(prices), k//2
        Sum=list(accumulate((strategy[i]*prices[i] for i in range(n)),initial=0))
        modify=sum(prices[k2:k])
        profit=max(Sum[n], modify+Sum[n]-Sum[k])

        for i in range(1, n+1-k):
            modify+=prices[i+k-1]-prices[i+k2-1]
            profit=max(profit, modify+Sum[n]-Sum[i+k]+Sum[i])
        return profit
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/submissions/1859190897/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

