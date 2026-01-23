

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Minimum Pair Removal to Sort Array II</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/submissions/1894459037/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-23T15:30:43.712Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3510. Minimum Pair Removal to Sort Array IISolvedHardTopicsCompaniesHintGiven an array nums, you can perform the following operation any number of times:


	Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
	Replace the pair with their sum.


Return the minimum number of operations needed to make the array non-decreasing.

An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

 
Example 1:


Input: nums = [5,2,3,1]

Output: 2

Explanation:


	The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
	The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].


The array nums became non-decreasing in two operations.


Example 2:


Input: nums = [1,2,2]

Output: 0

Explanation:

The array nums is already sorted.


 
Constraints:


	1 <= nums.length <= 105
	-109 <= nums[i] <= 109

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        arr = [int(x) for x in nums]
        removed = [False] * n
        heap = []
        asc = 0
        for i in range(1, n):
            heapq.heappush(heap, (arr[i - 1] + arr[i], i - 1))
            if arr[i] >= arr[i - 1]:
                asc += 1
        if asc == n - 1:
            return 0

        rem = n
        prev = [i - 1 for i in range(n)]
        nxt = [i + 1 for i in range(n)]

        while rem > 1:
            if not heap:
                break
            sumv, left = heapq.heappop(heap)
            right = nxt[left]
            if right >= n or removed[left] or removed[right] or arr[left] + arr[right] != sumv:
                continue

            pre = prev[left]
            after = nxt[right]

            if arr[left] <= arr[right]:
                asc -= 1
            if pre != -1 and arr[pre] <= arr[left]:
                asc -= 1
            if after != n and arr[right] <= arr[after]:
                asc -= 1

            arr[left] += arr[right]
            removed[right] = True
            rem -= 1

            if pre != -1:
                heapq.heappush(heap, (arr[pre] + arr[left], pre))
                if arr[pre] <= arr[left]:
                    asc += 1
            else:
                prev[left] = -1

            if after != n:
                prev[after] = left
                nxt[left] = after
                heapq.heappush(heap, (arr[left] + arr[after], left))
                if arr[left] <= arr[after]:
                    asc += 1
            else:
                nxt[left] = n

            if asc == rem - 1:
                return n - rem

        return n

```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/submissions/1894459037/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

