# Brute Force 100 %

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         # nums.sort()
#         n =len(nums)
#         return n*(n+1) //2 -sum(nums)

# Binary Search:
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        def customBinary(arr,l,r,n):



            m = l + (r-l)//2
            # print("Recursion Called", l , " + ", r, "+", m)
            # if l==m and r==m+1:
            #     return r
            if r<=l:
                return l
           
            if arr[m] == m:
                l=m+1
                return customBinary(arr,l,r,r)
        
            if arr[m]> m:
                r=m
                return customBinary(arr,l,r,r)
           

        ans = customBinary(nums,0, len(nums), len(nums))
        return ans
        