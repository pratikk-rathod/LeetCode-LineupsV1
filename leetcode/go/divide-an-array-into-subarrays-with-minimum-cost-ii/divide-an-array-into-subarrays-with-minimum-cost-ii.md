

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Divide an Array Into Subarrays With Minimum Cost II</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> go<br>
<b>Submitted:</b> 2026-02-02T18:28:10.531Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3013. Divide an Array Into Subarrays With Minimum Cost IISolvedHardTopicsCompaniesHintYou are given a 0-indexed array of integers nums of length n, and two positive integers k and dist.

The cost of an array is the value of its first element. For example, the cost of [1,2,3] is 1 while the cost of [3,4,1] is 3.

You need to divide nums into k disjoint contiguous subarrays, such that the difference between the starting index of the second subarray and the starting index of the kth subarray should be less than or equal to dist. In other words, if you divide nums into the subarrays nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ..., nums[ik-1..(n - 1)], then ik-1 - i1 <= dist.

Return the minimum possible sum of the cost of these subarrays.

 
Example 1:

Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
Output: 5
Explanation: The best possible way to divide nums into 3 subarrays is: [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist. The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.


Example 2:

Input: nums = [10,1,2,2,2,1], k = 4, dist = 3
Output: 15
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [1], [2], and [2,2,1]. This choice is valid because ik-1 - i1 is 3 - 1 = 2 which is less than dist. The total cost is nums[0] + nums[1] + nums[2] + nums[3] which is 10 + 1 + 2 + 2 = 15.
The division [10], [1], [2,2,2], and [1] is not valid, because the difference between ik-1 and i1 is 5 - 1 = 4, which is greater than dist.
It can be shown that there is no possible way to divide nums into 4 subarrays at a cost lower than 15.


Example 3:

Input: nums = [10,8,18,9], k = 3, dist = 1
Output: 36
Explanation: The best possible way to divide nums into 4 subarrays is: [10], [8], and [18,9]. This choice is valid because ik-1 - i1 is 2 - 1 = 1 which is equal to dist.The total cost is nums[0] + nums[1] + nums[2] which is 10 + 8 + 18 = 36.
The division [10], [8,18], and [9] is not valid, because the difference between ik-1 and i1 is 3 - 1 = 2, which is greater than dist.
It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 36.


 
Constraints:


	3 <= n <= 105
	1 <= nums[i] <= 109
	3 <= k <= n
	k - 2 <= dist <= n - 2

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```txt
class Solution:
    class SmartWindow:
        def __init__(self, k: int):
            self.K = k
            self.low = []   # sorted list
            self.high = []  # sorted list
            self.sumLow = 0

        def windowSize(self) -> int:
            return len(self.low) + len(self.high)

        def _erase_one(self, arr: List[int], x: int) -> bool:
            i = bisect_left(arr, x)
            if i < len(arr) and arr[i] == x:
                arr.pop(i)
                return True
            return False

        def rebalance(self) -> None:
            need = min(self.K, self.windowSize())

            while len(self.low) > need:
                x = self.low.pop()  # largest in low
                self.sumLow -= x
                insort(self.high, x)

            while len(self.low) < need and self.high:
                x = self.high.pop(0)  # smallest in high
                insort(self.low, x)
                self.sumLow += x

        def add(self, x: int) -> None:
            if not self.low or x <= self.low[-1]:
                insort(self.low, x)
                self.sumLow += x
            else:
                insort(self.high, x)
            self.rebalance()

        def remove(self, x: int) -> None:
            if self._erase_one(self.low, x):
                self.sumLow -= x
            else:
                self._erase_one(self.high, x)
            self.rebalance()

        def query(self) -> int:
            return self.sumLow

    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)
        k -= 1
        window = self.SmartWindow(k)

        for i in range(1, 1 + dist + 1):
            window.add(nums[i])

        ans = window.query()

        for i in range(2, n - dist):
            window.remove(nums[i - 1])
            window.add(nums[i + dist])
            ans = min(ans, window.query())

        return ans + nums[0]
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

