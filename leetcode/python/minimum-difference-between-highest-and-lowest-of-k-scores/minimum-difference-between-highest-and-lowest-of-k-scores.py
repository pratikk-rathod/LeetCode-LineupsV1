class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        lowest=9999999
        for i in range(len(nums)-k+1):

            lowest=min(nums[i+k-1]-nums[i], lowest)

        return lowest

        
        # return nums[-1]-nums[-k] if len(nums)>=k and k>1  else 0
        