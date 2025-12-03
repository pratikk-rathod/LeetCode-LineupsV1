

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Count Number of Trapezoids II</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/count-number-of-trapezoids-ii/submissions/1845956460/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-03T14:08:35.384Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3625. Count Number of Trapezoids IISolvedHardTopicsCompaniesHintYou are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

 
Example 1:


Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]

Output: 2

Explanation:

 

There are two distinct ways to pick four points that form a trapezoid:


	The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
	The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.



Example 2:


Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:



There is only one trapezoid which can be formed.


 
Constraints:


	4 <= points.length <= 500
	–1000 <= xi, yi <= 1000
	All points are pairwise distinct.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
from math import gcd
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        t = defaultdict(lambda: defaultdict(int))
        v = defaultdict(lambda: defaultdict(int))

        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy

                g = gcd(dx, abs(dy))
                sx = dx // g
                sy = dy // g

                des = sx * y1 - sy * x1

                key1 = (sx << 12) | (sy + 2000)
                key2 = (dx << 12) | (dy + 2000)

                t[key1][des] += 1
                v[key2][des] += 1

        return self.count(t) - self.count(v) // 2

    def count(self, mp):
        ans = 0

        for inner in mp.values():
            total = sum(inner.values())
            remaining = total

            for val in inner.values():
                remaining -= val
                ans += val * remaining

        return ans
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/count-number-of-trapezoids-ii/submissions/1845956460/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

