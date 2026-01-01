

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Same Tree</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/same-tree/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-01T19:12:11.806Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
100. Same TreeSolvedEasyTopicsCompaniesGiven the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 
Example 1:

Input: p = [1,2,3], q = [1,2,3]
Output: true


Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false


Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false


 
Constraints:


	The number of nodes in both trees is in the range [0, 100].
	-104 <= Node.val <= 104

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSame(self,l,r):
        
        if l==None and r ==None:
            return True
        elif l== None and r!=None :
            return False
        elif l!= None and r==None :
            return False
        return l.val==r.val and self.isSame(l.left, r.right) and self.isSame(l.right , r.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        l=root.left
        r=root.right

        return self.isSame(l, r)
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/same-tree/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

