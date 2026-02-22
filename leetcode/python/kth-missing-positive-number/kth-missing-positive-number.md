

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Kth Missing Positive Number</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/kth-missing-positive-number/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-02-22T14:30:38.977Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
Problem List
Debugging...
Submit
75
75Streaks
Already missing you!
13:27:20
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
1539. Kth Missing Positive Number
Solved
Easy

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        #binary SEarch
        l, r = 0, len(arr)-1
        if arr[r] == len(arr):
            return r +k+1
            #

        def bForMissing(arr, l ,r, k):
            m = l + (r-l)//2
            # print("here is the values of l,r ",l, r,m)
            # print(arr[:m], "upto m", arr[m]-1, len(arr[:m]))
            if l>=r:
                if k< arr[l] and k + len(arr[:l]) <arr[l]:
                    # print("coming here")
                    return len(arr[:l])+k
                else:
                    return arr[l] + (k - (arr[l] -len(arr[:l]))) +1
                # return l +k +1
            
            # if len(arr[:m]) == arr[m]-1:
            #     l=m+1
            #     # print('midddddddddd')
            #     return bForMissing(arr,l,r,k)
            
            if len(arr[:m]) < arr[m] -1 and k + len(arr[:m])+1 <= arr[m]:
                r=m
                # print("inf fffffff")                
                return bForMissing(arr,l,r,k)
            else:
                l=m+1
                # print("in else")
                return bForMissing(arr,l,r,k)

        return bForMissing(arr,l,r,k)



        # count=0
        # curr=arr[0]
        # curri=0
        # for i in range(1,arr[-1]+100000):
        #     if curri>=len(arr):
        #         break
        #     if i == arr[curri]:
        #         curri+=1
        #         continue
        #     if i !=arr[curri]:
        #         count+=1 
        #     if count == k:
        #         return i
            
        # ans=arr[-1]     
        # while count<k:
        #     count+=1
        #     ans+=1
        # return ans        

        # # Brute Force

        # # array=sorted(list(set([i for i in range(1,arr[-1]+10000)]) - set(arr)))
        # # return array[k-1]
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/kth-missing-positive-number/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

