# key takeaway:
# A number can have factorials till its Root(n) after that they will repeat
# Divisors mirror around √n.
# After √n, you only see the mirror image of what you already found.

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans=0

        for i in nums:
            arr=[]
            lenn=0

            for j in range(1,int(i**0.5)+1):
                if i%j ==0:
                    arr.append(j)
                    if j!= i//j:
                        arr.append(i//j)
                        lenn+=1
                    lenn+=1
                    if lenn>4:
                        break
            if lenn==4:
                ans+=sum(arr)
        return ans
            
        