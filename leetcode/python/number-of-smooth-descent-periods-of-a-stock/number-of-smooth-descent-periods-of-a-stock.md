

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Number of Smooth Descent Periods of a Stock</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/submissions/1856516423/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-15T18:08:27.560Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
2110. Number of Smooth Descent Periods of a StockSolvedMediumTopicsCompaniesHintYou are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.

 
Example 1:

Input: prices = [3,2,1,4]
Output: 7
Explanation: There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.


Example 2:

Input: prices = [8,6,7,7]
Output: 4
Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.


Example 3:

Input: prices = [1]
Output: 1
Explanation: There is 1 smooth descent period: [1]


 
Constraints:


	1 <= prices.length <= 105
	1 <= prices[i] <= 105

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # print(len(prices))
        if len(prices)==1:
            return 1
        if len(prices)==2:
            return 3 if prices[0]-1 == prices[1] else 2
        prices.append(0)
        prices.append(0)
        # prices.append(0)

        n=len(prices)
        if n==1:
            return 1
        dp=[0] * (n)
        temp=1
        # prev_val=prices[0]
        # curr_val=prices[1]
        for i in range(1,n):

            curr_val=prices[i]
            prev_val= prices[i-1]

            if curr_val +1 == prev_val:
                temp+=1
                continue
            else:
                print("here in temp")
                dp[i]= temp
                temp=1
        # if prices[-]
        # print(dp)


        # ans=n

        # for i in range(n):
        #     x=prices[i]
        #     for j in range(i+1,n):

        #         if x-1 == prices[j]:
        #             x=prices[j]
        #             ans+=1
        #         else:
        #             break\
        # print(dp[-1])
        isvalid =False
        if dp[-1]-1 == n -2:
            print("its true")
            isvalid=True
            # return sum(dp)
        for i, c in enumerate(dp):
            dp[i] = (dp[i]-1) * dp[i] //2
        # print("updated dp", dp        )

        if isvalid:
            return sum(dp)
        return n+ sum(dp) -2
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/submissions/1856516423/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

