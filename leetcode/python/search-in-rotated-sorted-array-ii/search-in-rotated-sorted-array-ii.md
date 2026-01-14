

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Search in Rotated Sorted Array II</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-14T03:07:27.853Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
81. Search in Rotated Sorted Array IISolvedMediumTopicsCompaniesThere is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 
Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

 
Constraints:


	1 <= nums.length <= 5000
	-104 <= nums[i] <= 104
	nums is guaranteed to be rotated at some pivot.
	-104 <= target <= 104


 
Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def binarySearch(nums,low, high) -> bool:
            # l=low
            # h=high

            while low+1< high and nums[low] == nums[low +1]:
                low=low+1
            
            while high-1>low and nums[high] == nums[high -1]:
                high = high-1

        

            if high<low:
                return False
            mid=low + (high-low)//2

            print(low, high , mid ,"printtin low high")

            

            if nums[mid] == target:
                return True
            
            if nums[low]<= nums[mid]:
                # if nums[low]>=target and target<nums[mid]:
                #     high = mid 
                #     return binarySearch(nums,low,high)0
                if nums[low]<=target and target<nums[mid]:
                    high=mid-1
                    return binarySearch(nums,low,high)
                else:
                    low=mid+1
                    return binarySearch(nums,low,high)
            
            else:
                if target>nums[mid] and target<=nums[high]:
                    low =mid+1
                    return binarySearch(nums,low,high)
                
                else:
                    high= mid-1
                    return binarySearch(nums,low,high)







        low,high = 0, len(nums)-1

        if len(nums) ==1 and nums[0] == target:
            return True
        elif len(nums) ==1 and nums[0] != target:
            return False

        ans = binarySearch(nums,low,high)

        return ans
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/search-in-rotated-sorted-array-ii/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

