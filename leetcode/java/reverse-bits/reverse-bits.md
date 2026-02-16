

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Reverse Bits</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/reverse-bits/submissions/1921184361/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> java<br>
<b>Submitted:</b> 2026-02-16T15:34:42.105Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
190. Reverse BitsSolvedEasyTopicsCompaniesReverse bits of a given 32 bits signed integer.

 
Example 1:


Input: n = 43261596

Output: 964176192

Explanation:

IntegerBinary432615960000001010010100000111101001110096417619200111001011110000010100101000000


Example 2:


Input: n = 2147483644

Output: 1073741822

Explanation:

IntegerBinary214748364401111111111111111111111111111100107374182200111111111111111111111111111110


 
Constraints:


	0 <= n <= 231 - 2
	n is even.


 
Follow up: If this function is called many times, how would you optimize it?

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```java
#BRUTE FORCE
class Solution:
    def reverseBits(self, n: int) -> int:

        ans = (bin(n)[:1:-1])

        x=32 - len(ans)
        print(ans)

        q=""
        for i in range(x):
            q+="0"
        return int(str((bin(n)[:1:-1])+q),2)
        
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/reverse-bits/submissions/1921184361/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

