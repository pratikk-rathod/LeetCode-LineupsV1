

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Approach (step-by-step)</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/longest-balanced-subarray-ii/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> go<br>
<b>Submitted:</b> 2026-02-11T20:15:35.543Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Daily Question
Judging...
Speed Up
Debugging...
Submit
63
63Streaks
Miss me yet?
07:07:23
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
Time Limit Exceeded
Time Limit Exceeded
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Code
Testcase
Testcase
Test Result
3721. Longest Balanced Subarray II
Attempted
Hard

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```txt
from typing import List
class SegTree:
    def __init__(self, n):
        self.n = n
        self.mn = [0] * (4*n)
        self.mx = [0] * (4*n)
        self.lazy = [0] * (4*n)
    def apply(self, idx, v):
        self.mn[idx] += v
        self.mx[idx] += v
        self.lazy[idx] += v
    def push(self, idx):
        z = self.lazy[idx]
        if z:
            self.apply(idx<<1, z)
            self.apply(idx<<1|1, z)
            self.lazy[idx] = 0
    def pull(self, idx):
        self.mn[idx] = min(self.mn[idx<<1], self.mn[idx<<1|1])
        self.mx[idx] = max(self.mx[idx<<1], self.mx[idx<<1|1])
    def add_range(self, idx, l, r, ql, qr, val):
        if ql > qr: return
        if ql <= l and r <= qr:
            self.apply(idx, val); return
        self.push(idx)
        mid = (l + r) >> 1
        if ql <= mid: self.add_range(idx<<1, l, mid, ql, min(qr, mid), val)
        if qr > mid:  self.add_range(idx<<1|1, mid+1, r, max(ql, mid+1), qr, val)
        self.pull(idx)
    def add(self, l, r, v):
        if l > r: return
        self.add_range(1, 0, self.n-1, l, r, v)
    def find_rightmost_zero(self, idx, l, r, ql, qr):
        if ql > qr or qr < l or ql > r: return -1
        if self.mn[idx] > 0 or self.mx[idx] < 0: return -1
        if l == r:
            return l if self.mn[idx] == 0 else -1
        self.push(idx)
        mid = (l + r) >> 1
        if qr > mid:
            res = self.find_rightmost_zero(idx<<1|1, mid+1, r, max(ql, mid+1), qr)
            if res != -1: return res
        if ql <= mid:
            return self.find_rightmost_zero(idx<<1, l, mid, ql, min(qr, mid))
        return -1
    def find(self, l, r):
        if l > r: return -1
        return self.find_rightmost_zero(1, 0, self.n-1, l, r)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        pos = {}
        for i, v in enumerate(nums):
            pos.setdefault(v, []).append(i)
        st = SegTree(n)
        for v, lst in pos.items():
            sign = 1 if (v & 1) else -1
            st.add(lst[0], n-1, sign)
        ptr = {v:0 for v in pos}
        ans = 0
        for l in range(n):
            r = st.find(l, n-1)
            if r != -1:
                ans = max(ans, r - l + 1)
            x = nums[l]
            pIndex = ptr[x]; ptr[x] = pIndex + 1
            lst = pos[x]
            nextPos = lst[ptr[x]] if ptr[x] < len(lst) else n
            sign = 1 if (x & 1) else -1
            L, R = l, nextPos - 1
            if L <= R:
                st.add(L, R, -sign)
        return ans
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/longest-balanced-subarray-ii/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

