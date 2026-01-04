

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Search Insert Position</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/search-insert-position/submissions/1874575156/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-04T18:58:19.832Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
35. Search Insert PositionSolvedEasyTopicsCompaniesGiven a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2


Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1


Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


 
Constraints:


	1 <= nums.length <= 104
	-104 <= nums[i] <= 104
	nums contains distinct values sorted in ascending order.
	-104 <= target <= 104

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         def binary(arr, l, r, target):
#             if r<l:
#                 return l
#             m= l + (r-l)//2
#             print(m)
#             if arr[m] == target:
#                 return m
#             if arr[m]>target:
#                 r=m-1
#                 return binary(arr,l,r,target)
            
#             if arr[m]<target:
#                 l=m+1
#                 return binary(arr,l,r,target)
            
        

#         ans = binary(nums,0,len(nums)-1,target)
#         return ans


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1

        m= l + (r-l)//2

        while r>=l:
            
            m= l + (r-l)//2

            if nums[m]==target:
                return m
            
            if nums[m]>target:
                r=m-1
            if nums[m]<target:
                l=m+1

   
        return r+1
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/search-insert-position/submissions/1874575156/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

