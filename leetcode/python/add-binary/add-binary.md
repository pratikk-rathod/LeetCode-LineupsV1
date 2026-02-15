

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Intuition</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/add-binary/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-02-15T19:37:11.955Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
67. Add BinarySolvedEasyTopicsCompaniesGiven two binary strings a and b, return their sum as a binary string.

 
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

 
Constraints:


	1 <= a.length, b.length <= 104
	a and b consist only of '0' or '1' characters.
	Each string does not contain leading zeros except for the zero itself.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         m = min(len(a),len(b))

#         ans=""
#         carry=0
#         for i in range(1,m+1):
#             print(ans)
#             # carry=0
#             if carry==0:
#                 if int(a[-m])==0 and int(b[-m])==0:
#                     carry=0
#                     ans+='0'
#                     continue

#                 if int(a[-m])==1 and int(b[-m])==1:
#                     carry=1
#                     ans+='0'
#                     continue
                
#                 if int(a[-m])==1 and int(b[-m])==0:
#                     carry=0
#                     ans+='1'
#                     continue

#                 if int(a[-m])==0 and int(b[-m])==1:
#                     carry=0
#                     ans+='1'
#                     continue

            
#             if carry==1:
#                 if int(a[-m])==0 and int(b[-m])==0:
#                     carry=0
#                     ans+='1'
#                     continue

#                 if int(a[-m])==1 and int(b[-m])==1:
#                     carry=1
#                     ans+='1'
#                     continue
                
#                 if int(a[-m])==1 and int(b[-m])==0:
#                     carry=1
#                     ans+='0'
#                     continue

#                 if int(a[-m])==0 and int(b[-m])==1:
#                     carry=1
#                     ans+='0'
#                     continue

        
#         if len(b)==m and len(a)>m:
#             m+=1
#             while m<len(a):
#                     # carry=0
#                 if carry==0:
#                     if int(a[-m])==0 and int(b[-m])==0:
#                         carry=0
#                         ans+='0'
#                         continue


#                     if int(a[-m])==1 and int(b[-m])==1:
#                         carry=1
#                         ans+='0'
#                         continue
                    
#                     if int(a[-m])==1 and int(b[-m])==0:
#                         carry=0
#                         ans+='1'
#                         continue

#                     if int(a[-m])==0 and int(b[-m])==1:
#                         carry=0
#                         ans+='1'
#                         continue
                
#                 if carry==1:
#                     if int(a[-m])==0 and int(b[-m])==0:
#                         carry=0
#                         ans+='1'
#                         continue

#                     if int(a[-m])==1 and int(b[-m])==1:
#                         carry=1
#                         ans+='1'
#                         continue
                    
#                     if int(a[-m])==1 and int(b[-m])==0:
#                         carry=1
#                         ans+='0'
#                         continue

#                     if int(a[-m])==0 and int(b[-m])==1:
#                         carry=1
#                         ans+='0'
#                         continue

                
#                 m+=1
            
#         if len(a)==m and len(b)>m:
                
#             m+=1
#             while m<len(b):
#                     # carry=0
#                 if carry==0:
#                     if int(a[-m])==0 and int(a[-m])==0:
#                         carry=0
#                         ans+='0'

#                     if int(a[-m])==1 and int(a[-m])==1:
#                         carry=1
#                         ans+='0'
                    
#                     if int(a[-m])==1 and int(a[-m])==0:
#                         carry=0
#                         ans+='1'
#                     if int(a[-m])==0 and int(a[-m])==1:
#                         carry=0
#                         ans+='1'
                
#                 if carry==1:
#                     if int(a[-m])==0 and int(a[-m])==0:
#                         carry=0
#                         ans+='1'

#                     if int(a[-m])==1 and int(a[-m])==1:
#                         carry=1
#                         ans+='1'
                    
#                     if int(a[-m])==1 and int(a[-m])==0:
#                         carry=1
#                         ans+='0'
#                     if int(a[-m])==0 and int(a[-m])==1:
#                         carry=1
#                         ans+='0'
                
#                 m+=1

        
#         return ans[::-1]
                
        
            
class Solution:
  
  def addBinary(self, a: str, b: str) -> str:
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(s))
    
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/add-binary/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

