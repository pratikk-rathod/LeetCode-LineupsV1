

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Count Covered Buildings</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/count-covered-buildings/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-11T15:59:32.328Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3531. Count Covered BuildingsSolvedMediumTopicsCompaniesHintYou are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

A building is covered if there is at least one building in all four directions: left, right, above, and below.

Return the number of covered buildings.

 
Example 1:




Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

Output: 1

Explanation:


	Only building [2,2] is covered as it has at least one building:

	
		above ([1,2])
		below ([3,2])
		left ([2,1])
		right ([2,3])
	
	
	Thus, the count of covered buildings is 1.



Example 2:




Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]

Output: 0

Explanation:


	No building has at least one building in all four directions.



Example 3:




Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

Output: 1

Explanation:


	Only building [3,3] is covered as it has at least one building:

	
		above ([1,3])
		below ([5,3])
		left ([3,2])
		right ([3,5])
	
	
	Thus, the count of covered buildings is 1.



 
Constraints:


	2 <= n <= 105
	1 <= buildings.length <= 105 
	buildings[i] = [x, y]
	1 <= x, y <= n
	All coordinates of buildings are unique.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xMax, yMax=[0]*(n+1), [0]*(n+1)
        xMin, yMin=[1<<31]*(n+1), [1<<31]*(n+1)

        for x, y in buildings:
            xMin[y]=min(xMin[y], x)
            xMax[y]=max(xMax[y], x)
            yMin[x]=min(yMin[x], y)
            yMax[x]=max(yMax[x], y)

        cnt=0
        for x, y in buildings:
            coverX=(xMin[y]<x & x<xMax[y])
            coverY=(yMin[x]<y & y<yMax[x])
            cnt+=(coverX & coverY)
        return cnt
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/count-covered-buildings/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

