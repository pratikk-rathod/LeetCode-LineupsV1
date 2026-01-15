

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Single Element in a Sorted Array</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/single-element-in-a-sorted-array/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-15T03:52:10.946Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
540. Single Element in a Sorted ArraySolvedMediumTopicsCompaniesYou are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10

 
Constraints:


	1 <= nums.length <= 105
	0 <= nums[i] <= 105

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
# 35 mines
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def customm(nums,l,r):

            m=l+(r-l)//2
            print(l,m,r,"l m r")
            if r<l:
                return nums[l]
            if m!=0 and m<len(nums)-1:
                if nums[m-1] == nums[m]:
                    if (m-l-1) %2 !=0:
                        print("insided if if")
                        return customm(nums,l,m-2)
                    else:
                        print("insided if else")
                        return customm(nums,m+1,r)
                elif nums[m+1] == nums[m]:
                    if (m-l-1) %2 !=0:
                        print("insided elif if")
                        return customm(nums,m+2,r)
                    else:
                        print("insided elif else")
                        return customm(nums,l,m-1)
                
                else:
                    print("i should be here")
                    return nums[m]

            return nums[r]

        l,r = 0, len(nums)-1

        return customm(nums,l,r)
        # a=list(set(nums))

        # for i in a:
        #     if nums.count(i)==1:
        #         return i

        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/single-element-in-a-sorted-array/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

