

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Number of Ways to Split a String</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/number-of-ways-to-split-a-string/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-15T16:58:08.418Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
1573. Number of Ways to Split a StringSolvedMediumTopicsCompaniesHintGiven a binary string s, you can split s into 3 non-empty strings s1, s2, and s3 where s1 + s2 + s3 = s.

Return the number of ways s can be split such that the number of ones is the same in s1, s2, and s3. Since the answer may be too large, return it modulo 109 + 7.

 
Example 1:

Input: s = "10101"
Output: 4
Explanation: There are four ways to split s in 3 parts where each part contain the same number of letters '1'.
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"


Example 2:

Input: s = "1001"
Output: 0


Example 3:

Input: s = "0000"
Output: 3
Explanation: There are three ways to split s in 3 parts.
"0|0|00"
"0|00|0"
"00|0|0"


 
Constraints:


	3 <= s.length <= 105
	s[i] is either '0' or '1'.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
# import math


# class Solution:
#     def numWays(self, s: str) -> int:
#         def binomial(x,k):
#             from math import factorial
#             return factorial(x) // (factorial(k) * factorial(x - k))
#         mod = 10 **9 +7
#         n= len(s)
#         summ=0
#         if s.count("1")>=1:
#             summ=s.count("1")
#         if summ%3 !=0:
#             return 0
#         if summ==0:
#             return binomial(n-1,2) % mod
#         ans=0
        
#         f_l=0
#         f_m=0
#         f_r=0
#         l=0
#         m=0
#         r=0

#         counterr=summ//3
#         tempc=0
#         firstc=0

#         for i in range(len(s)):

#             if s[i]=="1":
#                 tempc+=1
#                 if tempc==1:
#                     if f_l==0 and f_m==0 and f_r==0:
#                         f_l=i
#                     elif f_l!=0 and f_m==0 and f_r ==0:
#                         f_m=i
#                     elif f_l!=0 and f_m!= 0 and f_r==0:
#                         f_r=i
                 
#             firstc=tempc
#             # print(firstc)
#             if firstc==counterr:
#                 tempc=0
#                 if l==0 and m==0:
#                     l=i
#                     continue
#                 if m==0 and r ==0:
#                     m=i
#                     continue

#                 if r==0:
#                     r=i
#                     continue
#         if f_r==0:
#             f_l, f_r = f_r, f_l
#             f_m, f_r = f_r, f_m
#         if r==0:
#             l, r = r,l
#             m,r=r,m
#         print(l,m,r)
#         print(f_l,f_m,f_r)


#         ans = ((f_m - l)* (f_r -m )) % mod
#         return ans

# Enhanced version--->>>>>
# Enhanced version--->>>>>
# Enhanced version--->>>>>
# Enhanced version--->>>>>
# Enhanced version--->>>>>


import math


class Solution:
    def numWays(self, s: str) -> int:
        # def binomial(x,k):
        #     from math import factorial
        #     return factorial(x) // (factorial(k) * factorial(x - k))
        mod = 10 **9 +7
        n= len(s)
        summ=0
        if s.count("1")>=1:
            summ=s.count("1")
        if summ%3 !=0:
            return 0
        if summ==0:
            return ((n-1)*(n-2)//2) % mod
        ans=0
        arr=[i for i,c in enumerate(s) if c=="1"]
        print(arr)
        target= summ//3

        return (arr[target]- arr[target-1]) * (arr[2*target]- arr[2*target-1]) % mod
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/number-of-ways-to-split-a-string/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

