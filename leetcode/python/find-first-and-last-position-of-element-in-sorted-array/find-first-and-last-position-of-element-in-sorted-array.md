

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Find First and Last Position of Element in Sorted Array</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-04T19:53:24.615Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
34. Find First and Last Position of Element in Sorted ArraySolvedMediumTopicsCompaniesGiven an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

 
Constraints:


	0 <= nums.length <= 105
	-109 <= nums[i] <= 109
	nums is a non-decreasing array.
	-109 <= target <= 109

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:   
        
        
        low,high = 0, len(nums)-1
        stored=0
        occurance=0
        if high<low:
            return [-1,-1]
        while low <= high:
            m= low+ (high-low)//2
            if nums[m]==target:
                stored=m
                occurance+=1
                high=m-1
            if nums[m]> target:
                high=m-1
            if nums[m]<target:
                low=m+1
        # print(stored)
        low= stored
        high = len(nums)-1
        stored2=0
        
        while low <= high:
            m= low+ (high-low)//2
            # print(m)
            if nums[m]==target:
                stored2=m
                low=m+1
            if nums[m]> target:
                high=m-1
            if nums[m]<target:
                low=m+1
        if stored == stored2 and occurance !=1:
            return [-1,-1]
        return [stored,stored2]
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

