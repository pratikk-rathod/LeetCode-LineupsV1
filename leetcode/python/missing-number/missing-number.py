class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        n =len(nums)
        return n*(n+1) //2 -sum(nums)
        