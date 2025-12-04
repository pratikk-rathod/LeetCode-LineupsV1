

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Maximum Population Year</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/maximum-population-year/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-04T14:24:13.065Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Problem List
Debugging...
Submit
3
3Streaks
Practice Time!
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

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def maximumPopulation(self, logs):

        calendar={}
        min_year=logs[0][0]
        max_year=logs[0][1]

        for i in logs:
            if i[0] in calendar: calendar[i[0]] +=1 
            else: calendar[i[0]]=1
            if i[1] in calendar: calendar[i[1]]-=1 
            else: calendar[i[1]]=-1




            if i[0]<min_year : min_year = i[0]
            if i[1]>max_year : max_year = i[1] -1

       
        final_ans=logs[0][0]
        final_ans_index=0
        max_counter=0

        prefix_sum=[]
        best=0
        year=0
        curr=0
        for i in range(min_year, max_year+1):
            if i in calendar:
                curr += calendar[i]
                
                if curr> best:
                    best = curr

                    year= i

        return year
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/maximum-population-year/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

