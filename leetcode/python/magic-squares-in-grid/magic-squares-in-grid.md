

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Magic Squares In Grid</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/magic-squares-in-grid/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-30T19:41:40.554Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Daily Question
Debugging...
Submit
21
21Streaks
Protect your streak!
00:00:00
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

```python
class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ct = 0
        for i in range(0,len(grid)-2):
            for j in range(0,len(grid[i])-2):
                strs = grid[i][j:j+3] +  grid[i+1][j:j+3] + grid[i+2][j:j+3]
                t = set(strs)
                mx,mn = max(t),min(t)
                if(len(t)==9 and mx==9 and mn==1):
                    diag1 = grid[i+1][j+1] + grid[i][j] + grid[i+2][j+2]
                    diag2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
                    row1= sum(grid[i][j:j+3])
                    row2= sum(grid[i+1][j:j+3])
                    row3= sum(grid[i+2][j:j+3]) 
                    col1=grid[i][j]+grid[i+1][j]+grid[i+2][j]
                    col2=grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]
                    col3=grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2]
                    if(diag1==diag2 and diag2==row1 and row1==row2 and row2==row3 and row3==col1 and col1==col2 and col2==col3):
                        ct+=1
        return ct
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/magic-squares-in-grid/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

