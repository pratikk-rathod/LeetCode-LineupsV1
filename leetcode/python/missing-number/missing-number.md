

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Missing Number</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/missing-number/submissions/1869713733/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-30T19:43:00.944Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Binary Search
Debugging...
Submit
21
21Streaks
Already missing you!
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
Code

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
# Brute Force 100 %

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         # nums.sort()
#         n =len(nums)
#         return n*(n+1) //2 -sum(nums)

# Binary Search:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        def customBinary(arr,l,r,n):



            m = l + (r-l)//2
            # print("Recursion Called", l , " + ", r, "+", m)
            # if l==m and r==m+1:
            #     return r
            if r<=l:
                return l
           
            if arr[m] == m:
                l=m+1
                return customBinary(arr,l,r,r)
        
            if arr[m]> m:
                r=m
                return customBinary(arr,l,r,r)
           

        ans = customBinary(nums,0, len(nums), len(nums))
        return ans
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/missing-number/submissions/1869713733/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

