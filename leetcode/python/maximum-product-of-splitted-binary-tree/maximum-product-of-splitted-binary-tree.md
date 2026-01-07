

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Maximum Product of Splitted Binary Tree</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-07T19:27:57.791Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Daily Question
Debugging...
Submit
29
29Streaks
Protect your streak!
01:42:56
Pratik Rathod
Access all features with our Premium subscription!
My Lists
Notebook
Progress
Points
Try New Features
Orders
My Playgrounds
Settings
Appearance
Sign Out
Premium
Description
Editorial
Editorial
Solutions
Solutions

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        self.best = 0

        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        total = total_sum(root)

        def dfs(node):
            if not node:
                return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            self.best = max(self.best, s * (total - s))
            return s

        dfs(root)
        return self.best % MOD
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

