

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Count Complete Tree Nodes</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/count-complete-tree-nodes/submissions/1870546186/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> go<br>
<b>Submitted:</b> 2025-12-31T20:29:25.435Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
222. Count Complete Tree NodesSolvedEasyTopicsCompaniesGiven the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 
Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6


Example 2:

Input: root = []
Output: 0


Example 3:

Input: root = [1]
Output: 1


 
Constraints:


	The number of nodes in the tree is in the range [0, 5 * 104].
	0 <= Node.val <= 5 * 104
	The tree is guaranteed to be complete.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```txt
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr=[]
        self.answer=0
        # self.printt()

    def inOrderTreeTraversal(self,root):
            if root != None:

                self.inOrderTreeTraversal(root.left)
                self.answer+=1
                self.inOrderTreeTraversal(root.right)
            return self.answer
    def countNodes(self, root: Optional[TreeNode]) -> int:

        
        

        return self.inOrderTreeTraversal(root)

        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/count-complete-tree-nodes/submissions/1870546186/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

