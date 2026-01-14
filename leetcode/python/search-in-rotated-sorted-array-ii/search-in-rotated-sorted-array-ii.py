class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def binarySearch(nums,low, high) -> bool:
            # l=low
            # h=high

            while low+1< high and nums[low] == nums[low +1]:
                low=low+1
            
            while high-1>low and nums[high] == nums[high -1]:
                high = high-1

        

            if high<low:
                return False
            mid=low + (high-low)//2

            print(low, high , mid ,"printtin low high")

            

            if nums[mid] == target:
                return True
            
            if nums[low]<= nums[mid]:
                # if nums[low]>=target and target<nums[mid]:
                #     high = mid 
                #     return binarySearch(nums,low,high)0
                if nums[low]<=target and target<nums[mid]:
                    high=mid-1
                    return binarySearch(nums,low,high)
                else:
                    low=mid+1
                    return binarySearch(nums,low,high)
            
            else:
                if target>nums[mid] and target<=nums[high]:
                    low =mid+1
                    return binarySearch(nums,low,high)
                
                else:
                    high= mid-1
                    return binarySearch(nums,low,high)







        low,high = 0, len(nums)-1

        if len(nums) ==1 and nums[0] == target:
            return True
        elif len(nums) ==1 and nums[0] != target:
            return False

        ans = binarySearch(nums,low,high)

        return ans
        