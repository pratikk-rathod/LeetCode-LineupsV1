

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Sum of All Odd Length Subarrays</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/1845189787/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> java<br>
<b>Submitted:</b> 2025-12-02T16:31:48.439Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
1588. Sum of All Odd Length SubarraysSolvedEasyTopicsCompaniesHintGiven an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.

 
Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:

Input: arr = [10,11,12]
Output: 66


 
Constraints:


	1 <= arr.length <= 100
	1 <= arr[i] <= 1000


 
Follow up:

Could you solve this problem in O(n) time complexity?

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```java
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
# class Solution:
#     def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum=0
        prefix_sum_array=[0]
        ans=0
        for i in arr:
            prefix_sum+=i
            prefix_sum_array.append(prefix_sum)
        

        n=len(arr)

        if n%2==0:
            n-=1
        if n ==1 :
            return prefix_sum_array[-1]
        
        while n >=1:
            
            for i in range(0,len(arr)):

                print(i)
                if i + n >len(arr):
                   
                    break
                ans+= prefix_sum_array[i+n]
                ans -= prefix_sum_array[i]
            
            n-=2
        return ans

```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/sum-of-all-odd-length-subarrays/submissions/1845189787/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

