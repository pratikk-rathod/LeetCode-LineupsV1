

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Minimum Cost to Convert String I</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/minimum-cost-to-convert-string-i/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2026-01-29T18:13:48.557Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 
Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.


Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.


Example 3:

Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.


 
Constraints:


	1 <= source.length == target.length <= 105
	source, target consist of lowercase English letters.
	1 <= cost.length == original.length == changed.length <= 2000
	original[i], changed[i] are lowercase English letters.
	1 <= cost[i] <= 106
	original[i] != changed[i]

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(original)
        adj_dic = dict()
        head_dic = collections.defaultdict(list)
        for i in range(n):
            if ((original[i],changed[i]) in adj_dic):
                adj_dic[(original[i],changed[i])]= min(adj_dic[(original[i],changed[i])], cost[i])
            else:
                adj_dic[(original[i],changed[i])]= cost[i]
                head_dic[original[i]].append(changed[i])
        
        #print("head_dic", head_dic)
        #print("adj_dic", adj_dic)
        @cache
        def minCost(node1, node2) -> int:

            pq = [(0, node1)]
            cost_for_node = collections.defaultdict(lambda:math.inf)
            cost_for_node[node1] = 0
            while pq:
                curr_cost, curr_node = heappop(pq)
                if curr_cost > cost_for_node[curr_node]:
                    continue
                if curr_node == node2:
                    return curr_cost
                
                ls = head_dic[curr_node]
                for neighbor in ls:
                    cost = adj_dic[(curr_node, neighbor)]
                    new_cost = curr_cost + cost
                    if new_cost < cost_for_node[neighbor]:
                        cost_for_node[neighbor] = new_cost
                        heappush(pq, (new_cost, neighbor))
            return -1
    
        m = len(source)
        ans = 0
        for i in range(m):
            if source[i] != target[i]:
                t= minCost(source[i], target[i])
                #print(source[i], target[i], t)
                if t == -1:
                    return -1
                ans += t
        
        return ans
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/minimum-cost-to-convert-string-i/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

