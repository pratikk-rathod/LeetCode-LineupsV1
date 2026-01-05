

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Search in Rotated Sorted Array</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-05T19:50:38.382Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Problem List
Debugging...
Submit
27
27Streaks
Protect your streak!
00:06:23
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
    def search(self, nums: List[int], target: int) -> int:

        low,high= 0, len(nums)-1
        arr=nums
        def binarySearchModified(l,r, target):
            # print("fata")
            print(l,r)
            if l>r:
                return -1
            mid = l+(r-l)//2

            if nums[mid] == target:
                return mid
            
            if nums[l]<=nums[mid]:
                if target>= nums[l] and target<nums[mid]:
                    r=mid-1
                    return binarySearchModified(l,r,target)
                else:
                    l=mid+1
                    return binarySearchModified(l,r,target)
            else:
                if target>nums[mid] and target<=nums[r]:
                    l=mid+1
                    return binarySearchModified(l,r,target)
                else:
                    r=mid-1
                    return binarySearchModified(l,r,target)

            # if arr[l]>arr[mid] or arr[l]>arr[r]:
            #     if arr[l]== target:
            #         return l
            #     else:
            #         return binarySearchModified(l+1,r, target)
            
            # else:
            #     if arr[mid] == target:
            #         return mid
                
            #     if arr[mid]>target:
            #         return binarySearchModified(l,mid-1, target)

            #     if arr[mid]<target:
            #         return binarySearchModified(l+1,r, target)

        ans= binarySearchModified(low,high, target)
        print(ans)
        return binarySearchModified(low,high, target)
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/search-in-rotated-sorted-array/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

