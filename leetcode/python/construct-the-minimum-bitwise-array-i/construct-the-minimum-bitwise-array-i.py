class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans=[]

        for i in nums:
            found=False
            for k in range(1,i+1):
                if k | (k+1) ==i:
                    ans.append(k)
                    found=True
                    break
            if not found:
                ans.append(-1)
        return ans