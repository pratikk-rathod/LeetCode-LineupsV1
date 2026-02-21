

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Prime Number of Set Bits in Binary Representation</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> go<br>
<b>Submitted:</b> 2026-02-21T16:17:47.847Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Daily Question
Debugging...
Submit
73
73Streaks
Extend Your Streak!
07:20:12
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
762. Prime Number of Set Bits in Binary Representation
Easy

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```txt
#Brute Force

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        ans=0 

        for i in range(left, right+1):

            c=bin(i)[2:]
            coount = c.count('1')
            # print(coount)
            true=True
            if coount<=1:
                continue
            for j in range(2,coount):
                # print("inforlloooppp", coount, j)
                if coount % j ==0:
                    true=False
                    break
            # print(true)
            if true ==True:
                ans+=1
        return ans

```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

