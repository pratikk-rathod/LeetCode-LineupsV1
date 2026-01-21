

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Koko Eating Bananas</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/koko-eating-bananas/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-21T20:26:27.025Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Problem List
Debugging...
Submit
43
43Streaks
Well Done!
12:02:11
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
875. Koko Eating Bananas
Solved
Medium

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles)==h:
        #     return max(piles)
        # if len(piles)==1:
        #     return 2
        minn,maxx= 1, max(piles)

        while minn<maxx:

            mid = minn + (maxx -minn)//2

            ans=0

            for i in piles:
                temp=i//mid
                temp_rem = i% mid

                if temp==0 and temp_rem!=0:
                    ans+=1
                elif temp!=0 and temp_rem!=0:
                    ans+= temp+1
                elif temp!=0 and temp_rem==0:
                    print("here")
                    ans+= temp
                # print("temp",temp)
                # if temp == int(temp):
                #     ans+= int(temp)
                # if temp> int(temp):
                #     ans+=int(temp)+1
            # print(minn, maxx, mid , ans )
            print(ans)
            if ans < h:
                maxx=mid
            elif ans> h:
                minn=mid+1
            elif ans==h:
                maxx=mid
        return minn

    #     # return sum(piles)
    #     class Solution:
    # # import math

    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     minn=1
    #     maxx=max(piles)
    #     def isSufficientSpeed(cnt):
    #         temp=0
    #         for k in piles:
    #             temp+=ceil(k/cnt)
    #         return  temp<=h
        
    #     while minn<maxx:
    #         m=(minn+maxx)//2
    #         if isSufficientSpeed(m):
    #             maxx=m
    #         else:
    #             minn=m+1
            
                
            

    #     return minn
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/koko-eating-bananas/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

