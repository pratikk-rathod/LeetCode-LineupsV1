

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Four Divisors</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/four-divisors/submissions/1874509514/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-04T17:52:00.875Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
1390. Four DivisorsSolvedMediumTopicsCompaniesHintGiven an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 
Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.


Example 2:

Input: nums = [21,21]
Output: 64


Example 3:

Input: nums = [1,2,3,4,5]
Output: 0


 
Constraints:


	1 <= nums.length <= 104
	1 <= nums[i] <= 105

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
# key takeaway:
# A number can have factorials till its Root(n) after that they will repeat
# Divisors mirror around √n.
# After √n, you only see the mirror image of what you already found.

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans=0

        for i in nums:
            arr=[]
            lenn=0

            for j in range(1,int(i**0.5)+1):
                if i%j ==0:
                    arr.append(j)
                    if j!= i//j:
                        arr.append(i//j)
                        lenn+=1
                    lenn+=1
                    if lenn>4:
                        break
            if lenn==4:
                ans+=sum(arr)
        return ans
            
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/four-divisors/submissions/1874509514/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

