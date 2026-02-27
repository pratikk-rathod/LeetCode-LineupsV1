

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Minimum Operations to Equalize Binary String</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-02-27T04:32:22.673Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3666. Minimum Operations to Equalize Binary StringSolvedHardTopicsCompaniesHintYou are given a binary string s, and an integer k.

In one operation, you must choose exactly k different indices and flip each '0' to '1' and each '1' to '0'.

Return the minimum number of operations required to make all characters in the string equal to '1'. If it is not possible, return -1.

 
Example 1:


Input: s = "110", k = 1

Output: 1

Explanation:


	There is one '0' in s.
	Since k = 1, we can flip it directly in one operation.



Example 2:


Input: s = "0101", k = 3

Output: 2

Explanation:

One optimal set of operations choosing k = 3 indices in each operation is:


	Operation 1: Flip indices [0, 1, 3]. s changes from "0101" to "1000".
	Operation 2: Flip indices [1, 2, 3]. s changes from "1000" to "1111".


Thus, the minimum number of operations is 2.


Example 3:


Input: s = "101", k = 2

Output: -1

Explanation:

Since k = 2 and s has only one '0', it is impossible to flip exactly k indices to make all '1'. Hence, the answer is -1.


 
Constraints:


	1 <= s.length <= 10​​​​​​​5
	s[i] is either '0' or '1'.
	1 <= k <= s.length

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def minOperations(self, s: str, k: int) -> int:
        # O(n) time complexity
        # O(1) space complexity

        n = len(s)
        z = s.count('0')
        
        if n == k:
            if z == 0:
                return 0
            elif z == n:
                return 1
            else:
                return -1
        
        def ceil(x, y):
            return (x + y - 1) // y
        
        ans = inf
        
        if z % 2 == 0:
            m = max(ceil(z, k), ceil(z, n - k))
            if m % 2 == 1:
                m += 1
            ans = min(ans, m)
        
        if z % 2 == k % 2:
            m = max(ceil(z, k), ceil(n - z, n - k))
            if m % 2 == 0:
                m += 1
            ans = min(ans, m)
        
        return ans if ans < inf else -1
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

