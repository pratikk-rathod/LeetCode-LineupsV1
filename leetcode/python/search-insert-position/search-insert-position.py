# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         def binary(arr, l, r, target):
#             if r<l:
#                 return l
#             m= l + (r-l)//2
#             print(m)
#             if arr[m] == target:
#                 return m
#             if arr[m]>target:
#                 r=m-1
#                 return binary(arr,l,r,target)
            
#             if arr[m]<target:
#                 l=m+1
#                 return binary(arr,l,r,target)
            
        

#         ans = binary(nums,0,len(nums)-1,target)
#         return ans


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1

        m= l + (r-l)//2

        while r>=l:
            
            m= l + (r-l)//2

            if nums[m]==target:
                return m
            
            if nums[m]>target:
                r=m-1
            if nums[m]<target:
                l=m+1

   
        return r+1
        