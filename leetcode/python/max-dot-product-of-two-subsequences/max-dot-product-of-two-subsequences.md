

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Max Dot Product of Two Subsequences</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/max-dot-product-of-two-subsequences/submissions/1879065235/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-08T18:24:05.877Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.

Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.

Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.

 

Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        memo = [[float('-inf')] * m for _ in range(n)]
        
        def dp(i, j):
            if i == n or j == m:
                return float('-inf')
            
            if memo[i][j] != float('-inf'):
                return memo[i][j]
            
            memo[i][j] = max(
                nums1[i] * nums2[j] + max(dp(i + 1, j + 1), 0),
                dp(i + 1, j),  
                dp(i, j + 1), 
            )
            
            return memo[i][j]
        
        return dp(0, 0)
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/max-dot-product-of-two-subsequences/submissions/1879065235/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

