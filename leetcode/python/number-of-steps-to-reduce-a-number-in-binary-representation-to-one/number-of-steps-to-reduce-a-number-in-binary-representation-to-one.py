#Brute Force 
class Solution:
    def numSteps(self, s: str) -> int:
        s = int(str(s),2)
        # print(a)
        steps=0
        while s !=1:
            # print(a)

            if s %2 ==0:
                s //=2
            else:
                s+=1
                
            steps+=1
        return steps
        