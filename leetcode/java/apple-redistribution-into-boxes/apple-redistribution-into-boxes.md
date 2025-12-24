

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Apple Redistribution into Boxes</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/apple-redistribution-into-boxes/submissions/1864421431/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> java<br>
<b>Submitted:</b> 2025-12-24T18:13:28.844Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
3074. Apple Redistribution into BoxesSolvedEasyTopicsCompaniesHintYou are given an array apple of size n and an array capacity of size m.

There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.

Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.

Note that, apples from the same pack can be distributed into different boxes.

 
Example 1:

Input: apple = [1,3,2], capacity = [4,3,1,5,2]
Output: 2
Explanation: We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.


Example 2:

Input: apple = [5,5,5], capacity = [2,4,2,7]
Output: 4
Explanation: We will need to use all the boxes.


 
Constraints:


	1 <= n == apple.length <= 50
	1 <= m == capacity.length <= 50
	1 <= apple[i], capacity[i] <= 50
	The input is generated such that it's possible to redistribute packs of apples into boxes.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```java
class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        // int ans=0;
        int ans =0;
        int sum1 = 0;
        // summ=
        // Method 2: Using IntStream.of().sum()
        int sum2 = IntStream.of(apple).sum();
        // System.out.println("The sum using IntStream.of() is: " + sum2); // Output: 150
        Arrays.sort(capacity);
        System.out.println(capacity);
        for(int i=capacity.length-1;  i >= 0; i--){
        System.out.println("The sum using IntStream.of() is: " + i); // Output: 150
        sum1+= (capacity[i]);
        ans+=1;
        if(sum1>=sum2){
            return ans;
        }
        }
        return sum2;
    }
}
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/apple-redistribution-into-boxes/submissions/1864421431/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

