

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Minimum Number of Days to Make m Bouquets</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/submissions/1904688667/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-02-01T18:20:15.900Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
1482. Minimum Number of Days to Make m BouquetsSolvedMediumTopicsCompaniesHintYou are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

 
Example 1:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.


Example 2:

Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.


Example 3:

Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.


 
Constraints:


	bloomDay.length == n
	1 <= n <= 105
	1 <= bloomDay[i] <= 109
	1 <= m <= 106
	1 <= k <= n

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        minn=min(bloomDay)
        maxx=max(bloomDay)

        ans=1000000000000 
        tempArray=bloomDay

        def customBS(bloomDay,l,r):
            # print(notlocal ans)
            nonlocal ans
            if r<l:
                return
            tempcounter=0
            tempcounter2=0
            mid= l +(r-l)//2

            for i in range(len(bloomDay)):
                # print("tempcounter", tempcounter, tempcounter2,k)

                if bloomDay[i]<=mid:
                    tempcounter+=1
                    if tempcounter>=k:
                        tempcounter2+=1
                        tempcounter=0


                else:
                    tempcounter=0
            # print(ans, l , r , mid, "ans L R m")

            # print(tempcounter,tempcounter2)
            
            if tempcounter2>=m:
                ans=min(ans,mid)
                r=mid-1
                return customBS(bloomDay,l,r)
            if tempcounter2<m:
                l=mid+1
                return customBS(bloomDay,l,r)
        
        customBS(bloomDay,minn,maxx)
        if ans==1000000000000:
            return -1
        
        return ans
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/submissions/1904688667/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

