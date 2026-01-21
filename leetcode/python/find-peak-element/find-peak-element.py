class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        l,r, ans = 0, len(nums)-1,0

        while l<r:
            mid = l + (r-l)//2
            if nums[mid] < nums[mid+1]:
                l=mid+1
            
            else:
                r=mid
        return l

        # if len(nums)==1:
        #     return 0
        # ans=0
        # # for i in range(len(nums)-1):
        # #     if nums[i+1]>nums[i]:
        # #         ans=i+1
        # # return ans
        
        # def bS(nums,l,r,anss):
        #     # global ans
        #     nonlocal ans
            
        #     m = l + (r-l)//2
            
        #     if nums[m+1]>nums[m]:
        #         ans=m+1
        #     if r<=l or l==m:
        #         return        
            
        #     bS(nums,l,m,ans)
        #     bS(nums,m,r,ans)
        # bS(nums,0,len(nums)-1, ans)
        # return ans

# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         #Brute Force O(N)
#         ans=0
#         for i in range(len(nums)-1):
#             if nums[i+1]>nums[i]:
#                 ans=i+1
#         return ans
        