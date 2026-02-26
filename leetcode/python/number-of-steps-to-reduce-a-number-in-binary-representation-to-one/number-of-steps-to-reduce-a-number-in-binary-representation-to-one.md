

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ It's Medium Because You're Not Supposed To Use Big Int</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-02-26T03:35:31.590Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
1404. Number of Steps to Reduce a Number in Binary Representation to OneSolvedMediumTopicsCompaniesHintGiven the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:


	
	If the current number is even, you have to divide it by 2.
	
	
	If the current number is odd, you have to add 1 to it.
	


It is guaranteed that you can always reach one for all test cases.

 
Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  


Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  


Example 3:

Input: s = "1"
Output: 0


 
Constraints:


	1 <= s.length <= 500
	s consists of characters '0' or '1'
	s[0] == '1'

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
#Brute Force 
class Solution:
    def numSteps(self, s: str) -> int:
        s = int(str(s),2)
        # print(a)
        steps=0
        while s !=1:
            # print(a)

            if s %2 ==0:
                s //=2
            else:
                s+=1
                
            steps+=1
        return steps
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

