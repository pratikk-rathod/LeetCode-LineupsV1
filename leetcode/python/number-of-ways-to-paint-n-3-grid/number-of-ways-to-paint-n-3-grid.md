

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Intuition</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-03T19:01:56.653Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
1411. Number of Ways to Paint N × 3 GridSolvedHardTopicsCompaniesHintYou have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 
Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.


Example 2:

Input: n = 5000
Output: 30228214


 
Constraints:


	n == grid.length
	1 <= n <= 5000

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 1000000007
        x, y = 6, 6
        
        for i in range(2, n + 1):
            new_x = (3 * x + 2 * y) % MOD
            new_y = (2 * x + 2 * y) % MOD
            x, y = new_x, new_y
        
        return (x + y) % MOD
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

