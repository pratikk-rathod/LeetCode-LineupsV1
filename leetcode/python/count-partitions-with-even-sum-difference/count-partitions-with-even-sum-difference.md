

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Count Partitions with Even Sum Difference</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/count-partitions-with-even-sum-difference/submissions/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-05T06:50:13.503Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3432. Count Partitions with Even Sum DifferenceSolvedEasyTopicsCompaniesHintYou are given an integer array nums of length n.

A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:


	Left subarray contains indices [0, i].
	Right subarray contains indices [i + 1, n - 1].


Return the number of partitions where the difference between the sum of the left and right subarrays is even.

 
Example 1:


Input: nums = [10,10,3,7,6]

Output: 4

Explanation:

The 4 partitions are:


	[10], [10, 3, 7, 6] with a sum difference of 10 - 26 = -16, which is even.
	[10, 10], [3, 7, 6] with a sum difference of 20 - 16 = 4, which is even.
	[10, 10, 3], [7, 6] with a sum difference of 23 - 13 = 10, which is even.
	[10, 10, 3, 7], [6] with a sum difference of 30 - 6 = 24, which is even.



Example 2:


Input: nums = [1,2,2]

Output: 0

Explanation:

No partition results in an even sum difference.


Example 3:


Input: nums = [2,4,6,8]

Output: 3

Explanation:

All partitions result in an even sum difference.


 
Constraints:


	2 <= n == nums.length <= 100
	1 <= nums[i] <= 100

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix_sum=[]
        summ=0

        for i in nums:
            summ+=i
            prefix_sum.append(summ)
        print(prefix_sum)
        ans=0
        for i in range(len(prefix_sum) -1):
            if abs(2 * prefix_sum[i] - prefix_sum[-1]) %2 ==0:
                ans+=1
        return ans
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/count-partitions-with-even-sum-difference/submissions/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

