

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Balance a Binary Search Tree</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/balance-a-binary-search-tree/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> go<br>
<b>Submitted:</b> 2026-02-09T17:00:33.908Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Daily Question
Debugging...
Submit
61
61Streaks
Now or Never!
07:06:04
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
Submissions
Submissions
Code

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```txt
class Solution:
    def dfs(self,root,l):
        if root is None:
            return
        a = root.left
        b = root.right
        root.left = None
        root.right = None
        self.dfs(a,l)
        l.append(root)
        self.dfs(b,l)
    def balanceBST(self, root: TreeNode) -> TreeNode:
        l = []
        self.dfs(root,l)
        print(l[0])
        def helper(l,r,lst):
            if l > r:
                return None
            m = ((l+r)//2)
            ro = lst[m]
            ro.left = helper(l,m-1,lst)
            ro.right = helper(m+1,r,lst)
            return ro
        return helper(0,len(l)-1,l)   
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/balance-a-binary-search-tree/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

