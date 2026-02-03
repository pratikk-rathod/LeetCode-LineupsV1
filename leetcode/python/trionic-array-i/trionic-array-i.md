

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Trionic Array I</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/trionic-array-i/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-02-03T18:10:12.392Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Daily Question
Pending...
Speed Up
Debugging...
Submit
55
55Streaks
Ready to Practice?
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
Testcase
Testcase
Test Result
3637. Trionic Array I
Easy

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        counter=0
        isIncreasing=True
        isDecreasing=True

        Firstcheck=False
        prev=nums[0]
        # val=nums[1]
        # if val<prev:
        #     return False
        for key,val in enumerate(nums[1:]):
            if val==prev:
                return False
            # print(val,key)
            if counter>3:
                return False
            
            if val>prev:
                if isDecreasing == True:
                    counter+=1
                isIncreasing=True
                isDecreasing=False
                
                Firstcheck=True
            

            if Firstcheck==True:
                if val<prev:
                    if isIncreasing == True:
                        counter+=1
                    isIncreasing=False
                    isDecreasing=True
            else:
                return False
            prev=val

            
        return True if counter==3 else False
            

```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/trionic-array-i/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

