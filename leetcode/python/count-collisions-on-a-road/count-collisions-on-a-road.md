

<div style="border: 2px solid #00eaff; padding: 18px; border-radius: 10px; background: #0a0f1f; color: #e0faff;">

<h1 style="color:#00eaff;text-shadow:0 0 10px #00eaff;">⚡ Count Collisions on a Road</h1>

<div style="border-left:4px solid #ff0099; padding-left:12px; margin:10px 0;">
<b>Source:</b> <a href="https://leetcode.com/problems/count-collisions-on-a-road/submissions/1847045504/" style="color:#ff66cc;">LeetCode</a><br>
<b>Language:</b> python<br>
<b>Submitted:</b> 2025-12-04T18:40:04.585Z<br>


</div>

---

## <span style="color:#39ff14;text-shadow:0 0 8px #39ff14;">📘 Problem Statement</span>
2211. Count Collisions on a RoadSolvedMediumTopicsCompaniesHintThere are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.

The number of collisions can be calculated as follows:


	When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
	When a moving car collides with a stationary car, the number of collisions increases by 1.


After a collision, the cars involved can no longer move and will stay at the point where they collided. Other than that, cars cannot change their state or direction of motion.

Return the total number of collisions that will happen on the road.

 
Example 1:

Input: directions = "RLRSLL"
Output: 5
Explanation:
The collisions that will happen on the road are:
- Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2.
- Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
- Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
- Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision and get hit by car 5. The number of collisions becomes 4 + 1 = 5.
Thus, the total number of collisions that will happen on the road is 5. 


Example 2:

Input: directions = "LLRR"
Output: 0
Explanation:
No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.

 
Constraints:


	1 <= directions.length <= 105
	directions[i] is either 'L', 'R', or 'S'.

---

## <span style="color:#ff0099;text-shadow:0 0 8px #ff0099;">💡 Solution Code</span>

```python
class Solution: 
    def countCollisions(self, directions: str) -> int:
        # BRUTE FORCE

        stack=[]
        colision=0
        for i in directions:
            # print(stack)
            if len(stack)==0:
                stack.append(i)
                continue
            
            if i == "L":
                if stack[-1] == "L":
                    stack.append("L")
                    continue
                elif stack[-1] == "S":
                    stack.append("S")
                    colision+=1
                    continue
                elif stack[-1] == "R":
                    # colision+=1
                    count=0


                    idx = len(stack) - 1
                    while idx >= 0 and stack[idx] == "R":
                        count += 1
                        idx -= 1
                    for j in range(count):
                        stack.pop()
                    colision+=(count)+1


                    stack.append("S")


                    # colision+=2
                    continue


            if i == "R":
                if stack[-1] == "R":
                    stack.append("R")
                    continue
                elif stack[-1] == "S":
                    stack.append("R")
                    # colision+=1
                    continue
                elif stack[-1] == "L":
                    # colision+=1
                    stack.append("R")
                    continue


            if i == "S":
                
                if stack[-1] == "R": 

                    count=0


                    idx = len(stack) - 1
                    while idx >= 0 and stack[idx] == "R":
                        count += 1
                        idx -= 1
                    for j in range(count):
                        stack.pop()
                    colision+=(count)


                    # stack.append("S")


                    stack.append("S")
                    # colision+=1
                    continue
                
                else:
                    stack.append("S")
                    continue


        return colision
```

---

## <span style="color:#00eaff;text-shadow:0 0 8px #00eaff;">📎 Notes</span>

- Original problem: <a href="https://leetcode.com/problems/count-collisions-on-a-road/submissions/1847045504/" style="color:#ff66cc;">LeetCode Link</a>  
- Auto-saved via <b style="color:#39ff14;">GitLeet Sync</b>  
- Developed by <b style="color:#ff0099;">Pratik Rathod</b>  


---

## <span style="color:#ff66cc;text-shadow:0 0 8px #ff66cc;">🔗 Connect With Me</span>

- <b>LinkedIn:</b> <a href="https://linkedin.com/in/pratikk-rathod" style="color:#00eaff;">Linkedin</a>  
- <b>LeetCode Profile:</b> <a href="https://leetcode.com/pratikk_rathod" style="color:#39ff14;">LeetCode</a>

</div>

