

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Count Partitions with Even Sum Difference</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/count-partitions-with-even-sum-difference/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-05T06:50:57.049Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Problem List
Debugging...
Submit
5
5Streaks
Come back soon!
04:51:17
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
Testcase
Testcase
Test Result
3432. Count Partitions with Even Sum Difference
Solved
Easy

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix_sum=[]
        summ=0

        for i in nums:
            summ+=i
            prefix_sum.append(summ)
        print(prefix_sum)
        ans=0
        for i in range(len(prefix_sum) -1):
            if (2 * prefix_sum[i] - prefix_sum[-1]) %2 ==0:
                ans+=1
        return ans
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/count-partitions-with-even-sum-difference/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

