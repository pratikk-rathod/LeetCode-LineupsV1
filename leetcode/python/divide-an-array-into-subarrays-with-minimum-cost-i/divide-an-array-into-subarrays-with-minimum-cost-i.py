class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        count=1
        ans=nums[0]

        n=len(nums)
        y=nums[1:]
        y.sort()
        return ans+sum(y[0:2])
        