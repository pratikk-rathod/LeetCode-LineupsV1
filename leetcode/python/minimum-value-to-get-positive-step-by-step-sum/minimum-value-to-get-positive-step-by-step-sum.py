class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum=0
        ans=0
        cond=False
        for i in nums:
            prefix_sum += i

            if prefix_sum< 1 :
                while prefix_sum <1:
                    prefix_sum+=1
                    ans+=1
                cond=True
        if cond == False:
            return 1
        return ans
        