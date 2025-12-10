

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Intuition</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-10T17:27:40.491Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
You are given an array complexity of length n.

There are n locked computers in a room with labels from 0 to n - 1, each with its own unique password. The password of the computer i has a complexity complexity[i].

The password for the computer labeled 0 is already decrypted and serves as the root. All other computers must be unlocked using it or another previously unlocked computer, following this information:


	You can decrypt the password for the computer i using the password for computer j, where j is any integer less than i with a lower complexity. (i.e. j < i and complexity[j] < complexity[i])
	To decrypt the password for computer i, you must have already unlocked a computer j such that j < i and complexity[j] < complexity[i].


Find the number of permutations of [0, 1, 2, ..., (n - 1)] that represent a valid order in which the computers can be unlocked, starting from computer 0 as the only initially unlocked one.

Since the answer may be large, return it modulo 109 + 7.

Note that the password for the computer with label 0 is decrypted, and not the computer with the first position in the permutation.

 
Example 1:


Input: complexity = [1,2,3]

Output: 2

Explanation:

The valid permutations are:


	[0, 1, 2]
	
		Unlock computer 0 first with root password.
		Unlock computer 1 with password of computer 0 since complexity[0] < complexity[1].
		Unlock computer 2 with password of computer 1 since complexity[1] < complexity[2].
	
	
	[0, 2, 1]
	
		Unlock computer 0 first with root password.
		Unlock computer 2 with password of computer 0 since complexity[0] < complexity[2].
		Unlock computer 1 with password of computer 0 since complexity[0] < complexity[1].
	
	



Example 2:


Input: complexity = [3,3,3,4,4,4]

Output: 0

Explanation:

There are no possible permutations which can unlock all computers.


 
Constraints:


	2 <= complexity.length <= 105
	1 <= complexity[i] <= 109

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution:
    def countPermutations(self, x: List[int]) -> int:
        return 0 if x[0]>=min(x[1:]) else factorial(len(x)-1)%(10**9+7)
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

