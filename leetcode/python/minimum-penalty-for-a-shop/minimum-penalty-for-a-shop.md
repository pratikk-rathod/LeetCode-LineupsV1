

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Minimum Penalty for a Shop</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/minimum-penalty-for-a-shop/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-26T17:00:03.496Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
2483. Minimum Penalty for a ShopSolvedMediumTopicsCompaniesHintYou are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':


	if the ith character is 'Y', it means that customers come at the ith hour
	whereas 'N' indicates that no customers come at the ith hour.


If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:


	For every hour when the shop is open and no customers come, the penalty increases by 1.
	For every hour when the shop is closed and customers come, the penalty increases by 1.


Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

 
Example 1:

Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.


Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.

Example 3:

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.


 
Constraints:


	1 <= customers.length <= 105
	customers consists only of characters 'Y' and 'N'.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
# class Solution:
#     def bestClosingTime(self, customers: str) -> int:
#         lem=len(customers)
#         penalties={}
#         counter=0

#         for i in range(len(customers)+1):
#             penalty=0
#             if i==0:
#                 for j in customers:
#                     if j=="Y":
#                         penalty+=1
#                 penalties[0]=penalty
#                 continue            
#             else:
                    
#                 for j in range(len(customers)):
                    
#                     if counter<j:
#                         if customers[j]=="Y":
#                             penalty+=1
#                     if counter>j:
#                         if customers[j]=="N":
#                             penalty+=1
#                     if counter==j:
#                         if customers[j]=="N":
#                             penalty+=1
#                 penalties[i]=penalty
#                 counter+=1

#         # print(penalties)
#         maxx=min(penalties.values())
#         for key,value in penalties.items():
#             if value==maxx:
#                 return key

#         # return maxx
        

class Solution:
    def bestClosingTime(self, cust: str) -> int:
        
        x = y = z = 0
        for i, charr in enumerate(cust):     
            z += (charr == "Y") * 2 - 1       
            if z > y:                       
                y, x = z, i+1               
        return x
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/minimum-penalty-for-a-shop/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

