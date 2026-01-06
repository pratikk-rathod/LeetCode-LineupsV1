

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Maximum Level Sum of a Binary Tree</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> go<br>
<b>Submitted:</b> 2026-01-06T19:58:02.406Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
1161. Maximum Level Sum of a Binary TreeSolvedMediumTopicsCompaniesHintGiven the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 
Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.


Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2


 
Constraints:


	The number of nodes in the tree is in the range [1, 104].
	-105 <= Node.val <= 105

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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # count=1
        ans=root.val
        level=1
        arr=[[root]]
        max_level=1
        while len(arr)>=1:
           
            curr = arr[0]
            temp=[]
            temp_ans=0

            # print(curr)
            while curr:
                root=curr.pop(0)
                temp_ans+=root.val
               

                if root.left:
                    temp.append(root.left)
                if root.right:
                    temp.append(root.right)
           
            arr.pop(0)
            level+=1
            if temp_ans > ans:
                ans=temp_ans
                max_level=level
            if temp!=[]:
                # ans=max(ans,temp_ans)
                
                    
                arr.append(temp)
            

        if max_level==1:
            return 1
        return max_level-1
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

