

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Maximal Rectangle</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/maximal-rectangle/submissions/1881649569/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-11T10:01:21.929Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Daily Question
Debugging...
Submit
32
0Streaks
Now or Never!
01:13:25
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
Code

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def NSL(arr):
            s = []
            res = []
            for i in range(len(arr)):
                if len(s) == 0:
                    res.append(-1)
                if len(s) > 0 and arr[i] > s[-1][0]:
                    res.append(s[-1][1])
                if len(s) > 0 and arr[i] <= s[-1][0]:
                    while len(s) > 0 and arr[i] <= s[-1][0]:
                        s.pop()
                    if len(s) == 0:
                        res.append(-1)
                    else:
                        res.append(s[-1][1])
                s.append([arr[i], i])
            return res


        def NSR(arr):
            s = []
            res = []
            j = len(arr) - 1
            while j >= 0:
                if len(s) == 0:
                    res.append(len(arr))
                if len(s) > 0 and arr[j] > s[-1][0]:
                    res.append(s[-1][1])
                if len(s) > 0 and arr[j] <= s[-1][0]:
                    while len(s) > 0 and arr[j] <= s[-1][0]:
                        s.pop()
                    if len(s) == 0:
                        res.append(len(arr))
                    else:
                        res.append(s[-1][1])
                s.append([arr[j], j])
                j -= 1
            res.reverse()
            return res


        def width(l, r):
            w = []
            for i in range(len(l)):
                Width = r[i] - l[i] - 1
                w.append(Width)
            return w


        def Area(arr,w):
            maxArea = 0
            for i in range(len(arr)):
                a = arr[i] * w[i]
                maxArea = max(maxArea,a)
            return maxArea


        def MAH(arr):
            left = NSL(arr)
            right = NSR(arr)
            Width = width(left,right)
            mxArea = Area(arr,Width)
            return mxArea


        def main(arr):
            row = [0] * len(arr[0])
            areaMax = 0
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if int(arr[i][j]) == 0:
                        row[j] = 0
                    row[j] = row[j] + int(arr[i][j])
                areaMax = max(areaMax,MAH(row))
            return areaMax

        return main(matrix)
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/maximal-rectangle/submissions/1881649569/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

