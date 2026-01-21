

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Find Peak Element</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/find-peak-element/submissions/1892564869/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-21T19:27:02.861Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Problem List
Debugging...
Submit
43
43Streaks
Well Done!
12:02:11
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
    def findPeakElement(self, nums: List[int]) -> int:

        l,r, ans = 0, len(nums)-1,0

        while l<r:
            mid = l + (r-l)//2
            if nums[mid] < nums[mid+1]:
                l=mid+1
            
            else:
                r=mid
        return l

        # if len(nums)==1:
        #     return 0
        # ans=0
        # # for i in range(len(nums)-1):
        # #     if nums[i+1]>nums[i]:
        # #         ans=i+1
        # # return ans
        
        # def bS(nums,l,r,anss):
        #     # global ans
        #     nonlocal ans
            
        #     m = l + (r-l)//2
            
        #     if nums[m+1]>nums[m]:
        #         ans=m+1
        #     if r<=l or l==m:
        #         return        
            
        #     bS(nums,l,m,ans)
        #     bS(nums,m,r,ans)
        # bS(nums,0,len(nums)-1, ans)
        # return ans

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         #Brute Force O(N)
#         ans=0
#         for i in range(len(nums)-1):
#             if nums[i+1]>nums[i]:
#                 ans=i+1
#         return ans
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/find-peak-element/submissions/1892564869/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

