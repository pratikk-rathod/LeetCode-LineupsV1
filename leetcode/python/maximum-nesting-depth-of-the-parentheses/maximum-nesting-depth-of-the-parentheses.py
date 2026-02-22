class Solution:
    def maxDepth(self, s: str) -> int:

        maxdepth=0

        ans =0 

        for i in s:
            if i =="(":
                ans+=1
            
            if i ==")":
                maxdepth = max(ans, maxdepth)
                ans-=1
            
        return maxdepth
        