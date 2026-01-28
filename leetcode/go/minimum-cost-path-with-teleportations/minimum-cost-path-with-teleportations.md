

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Intuition</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/minimum-cost-path-with-teleportations/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> go<br>
<b>Submitted:</b> 2026-01-28T18:55:54.636Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3651. Minimum Cost Path with TeleportationsSolvedHardTopicsCompaniesHintYou are given a m x n 2D integer array grid and an integer k. You start at the top-left cell (0, 0) and your goal is to reach the bottom‐right cell (m - 1, n - 1).

There are two types of moves available:


	
	Normal move: You can move right or down from your current cell (i, j), i.e. you can move to (i, j + 1) (right) or (i + 1, j) (down). The cost is the value of the destination cell.
	
	
	Teleportation: You can teleport from any cell (i, j), to any cell (x, y) such that grid[x][y] <= grid[i][j]; the cost of this move is 0. You may teleport at most k times.
	


Return the minimum total cost to reach cell (m - 1, n - 1) from (0, 0).

 
Example 1:


Input: grid = [[1,3,3],[2,5,4],[4,3,5]], k = 2

Output: 7

Explanation:

Initially we are at (0, 0) and cost is 0.

Current PositionMoveNew PositionTotal Cost(0, 0)Move Down(1, 0)0 + 2 = 2(1, 0)Move Right(1, 1)2 + 5 = 7(1, 1)Teleport to (2, 2)(2, 2)7 + 0 = 7

The minimum cost to reach bottom-right cell is 7.


Example 2:


Input: grid = [[1,2],[2,3],[3,4]], k = 1

Output: 9

Explanation: 

Initially we are at (0, 0) and cost is 0.

Current PositionMoveNew PositionTotal Cost(0, 0)Move Down(1, 0)0 + 2 = 2(1, 0)Move Right(1, 1)2 + 3 = 5(1, 1)Move Down(2, 1)5 + 4 = 9

The minimum cost to reach bottom-right cell is 9.


 
Constraints:


	2 <= m, n <= 80
	m == grid.length
	n == grid[i].length
	0 <= grid[i][j] <= 104
	0 <= k <= 10

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```txt
from collections import defaultdict

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        """
        suppose dp[i][j] yields the minimum cost to reach i, j
        then when k = 0, this is a dp problem where
        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        """
        m, n = len(grid), len(grid[0])
        # construct the teleportation order
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[grid[i][j]].append((i, j))
        
        # construct costs for k = 0
        inf = float('inf')
        dp = [[inf] * n for _ in range(m)]
        dp[0][0] = 0
        def update():
            for i in range(m):
                for j in range(n):
                    temp = grid[i][j] + min(
                        dp[i-1][j] if i else inf, 
                        dp[i][j-1] if j else inf
                    )
                    if temp < dp[i][j]: dp[i][j] = temp
        update()

        # teleport k times
        keys = sorted(d, reverse=True)
        for _ in range(k):
            dist = inf
            for key in keys:
                for i, j in d[key]:
                    if dp[i][j] < dist: dist = dp[i][j]
                for i, j in d[key]:
                    dp[i][j] = dist
            update()
        return dp[-1][-1]
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/minimum-cost-path-with-teleportations/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

