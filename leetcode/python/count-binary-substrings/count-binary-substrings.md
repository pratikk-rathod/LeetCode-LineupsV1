

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Count Binary Substrings</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/count-binary-substrings/submissions/1923920368/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-02-19T04:18:50.102Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
696. Count Binary SubstringsSolvedEasyTopicsCompaniesHintGiven a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 
Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.


Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.


 
Constraints:


	1 <= s.length <= 105
	s[i] is either '0' or '1'.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s+="9"
        ans=0
        c0=0
        c1=0
        prev=s[0]
        for i in range(len(s)):
            if prev!=s[i]:
                if c0!=0 and c1!=0:
                    ans+=min(c0,c1)
                if s[i]=="1":
                    c1=0
                if s[i]=="0":
                    c0=0
               
            if s[i]=="0":
                c0+=1
            if s[i]=="1":
                c1+=1
            prev=s[i]
            
       
        return ans




         #     temp=s[i]
        #     counter=1
        #     isTrue=True
        #     counter2=0
          
        #     for j in range(i+1,len(s)):


        #         if counter == counter2:
                   
        #             break
               
        #         if s[j] == temp:
        #             if isTrue==False:
                        
        #                 break
        #             counter +=1
        #         else:
        #             counter2+=1
        #             isTrue=False
        #     if counter == counter2:
        #         ans+=1
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/count-binary-substrings/submissions/1923920368/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

