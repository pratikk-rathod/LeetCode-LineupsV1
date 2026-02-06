

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Intuition</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/minimum-removals-to-balance-array/submissions/1910631209/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-02-06T19:05:45.044Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3634. Minimum Removals to Balance ArraySolvedMediumTopicsCompaniesHintYou are given an integer array nums and an integer k.

An array is considered balanced if the value of its maximum element is at most k times the minimum element.

You may remove any number of elements from nums​​​​​​​ without making it empty.

Return the minimum number of elements to remove so that the remaining array is balanced.

Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

 
Example 1:


Input: nums = [2,1,5], k = 2

Output: 1

Explanation:


	Remove nums[2] = 5 to get nums = [2, 1].
	Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.



Example 2:


Input: nums = [1,6,2,9], k = 3

Output: 2

Explanation:


	Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
	Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.



Example 3:


Input: nums = [4,6], k = 2

Output: 0

Explanation:


	Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.



 
Constraints:


	1 <= nums.length <= 105
	1 <= nums[i] <= 109
	1 <= k <= 105

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0]*k>=nums[-1]: return 0
        n=len(nums)
        ans=n
        l=0
        for r, x in enumerate(nums):
            while l<r and nums[l]*k<x:
                l+=1
            ans=min(ans, n-r+l-1)
        return ans
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/minimum-removals-to-balance-array/submissions/1910631209/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

