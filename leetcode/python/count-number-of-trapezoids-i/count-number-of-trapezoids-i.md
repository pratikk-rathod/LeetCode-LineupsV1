

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ ❌ Why TLE happens with nested loops</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/count-number-of-trapezoids-i/submissions/1844991068/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-02T12:15:47.568Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3623. Count Number of Trapezoids ISolvedMediumTopicsCompaniesHintYou are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the  number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 109 + 7.

 
Example 1:


Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:

  

There are three distinct ways to pick four points that form a horizontal trapezoid:


	Using points [1,0], [2,0], [3,2], and [2,2].
	Using points [2,0], [3,0], [3,2], and [2,2].
	Using points [1,0], [3,0], [3,2], and [2,2].



Example 2:


Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:



There is only one horizontal trapezoid that can be formed.


 
Constraints:


	4 <= points.length <= 105
	–108 <= xi, yi <= 108
	All points are pairwise distinct.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution(object):
    def countTrapezoids(self, points):
        MOD = 10**9 + 7
        from collections import Counter
        
        ycount = Counter(y for _, y in points)

        combos = []
        for cnt in ycount.values():
            if cnt >= 2:
                combos.append(cnt * (cnt - 1) // 2)

        if len(combos) < 2:
            return 0

        total_sum = 0
        sum_squares = 0

        for c in combos:
            c_mod = c % MOD
            total_sum = (total_sum + c_mod) % MOD
            sum_squares = (sum_squares + (c_mod * c_mod) % MOD) % MOD

        result = (total_sum * total_sum - sum_squares) % MOD
        result = result * pow(2, MOD - 2, MOD)  

        return result % MOD

```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/count-number-of-trapezoids-i/submissions/1844991068/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

