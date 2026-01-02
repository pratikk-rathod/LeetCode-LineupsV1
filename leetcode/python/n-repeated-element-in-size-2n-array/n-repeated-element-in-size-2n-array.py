class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        nums.sort()
        for i, val in enumerate(nums):
            prev=i
            nextt=i+1

            if val==nums[nextt]:
                return val
        return 3