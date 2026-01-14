# Brute Force
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[0]

class Solution:
    def findMin(self, nums: List[int]) -> int:

        def binarySearch(nums,low,high,temp):
            if high<=low:
                return nums[low]
            
            mid = low + (high-low)//2

            print(low,mid, high)

            if nums[low]<= nums[mid] and nums[mid] <= nums[high]:

                high=mid-1
                return binarySearch(nums,low,high,temp)

            elif nums[low]<= nums[mid] and nums[mid] >= nums[high]:
                low=mid+1
                
                return binarySearch(nums,low,high,temp)
            else:
                low=low+1
                return binarySearch(nums,low,high,temp)


        

        low,high = 0, len(nums)-1

        return binarySearch(nums,low,high,0)