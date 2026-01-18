class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Brute Force O(N)
        ans=0
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                ans=i+1
        return ans
        