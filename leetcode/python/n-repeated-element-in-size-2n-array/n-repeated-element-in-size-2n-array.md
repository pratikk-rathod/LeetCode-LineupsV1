

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ N-Repeated Element in Size 2N Array</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/1872457127/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-02T20:00:53.765Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
961. N-Repeated Element in Size 2N ArraySolvedEasyTopicsCompaniesYou are given an integer array nums with the following properties:


	nums.length == 2 * n.
	nums contains n + 1 unique elements.
	Exactly one element of nums is repeated n times.


Return the element that is repeated n times.

 
Example 1:
Input: nums = [1,2,3,3]
Output: 3
Example 2:
Input: nums = [2,1,2,5,3,2]
Output: 2
Example 3:
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5

 
Constraints:


	2 <= n <= 5000
	nums.length == 2 * n
	0 <= nums[i] <= 104
	nums contains n + 1 unique elements and one of them is repeated exactly n times.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        for i, val in enumerate(nums):
            prev=i
            nextt=i+1

            if val==nums[nextt]:
                return val
        return 3
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/1872457127/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

