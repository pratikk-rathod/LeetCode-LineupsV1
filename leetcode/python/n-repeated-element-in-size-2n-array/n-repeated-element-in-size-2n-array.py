class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        dictt={}

        for i in nums:
            if i in dictt:
                return i
            else:
                dictt[i]=0
    
#         nums.sort()
#         for i, val in enumerate(nums):
#             prev=i
#             nextt=i+1

#             if val==nums[nextt]:
#                 return val
#         return 3

