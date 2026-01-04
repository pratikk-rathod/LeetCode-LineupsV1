class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:   
        
        
        low,high = 0, len(nums)-1
        stored=0
        occurance=0
        if high<low:
            return [-1,-1]
        while low <= high:
            m= low+ (high-low)//2
            if nums[m]==target:
                stored=m
                occurance+=1
                high=m-1
            if nums[m]> target:
                high=m-1
            if nums[m]<target:
                low=m+1
        # print(stored)
        low= stored
        high = len(nums)-1
        stored2=0
        
        while low <= high:
            m= low+ (high-low)//2
            # print(m)
            if nums[m]==target:
                stored2=m
                low=m+1
            if nums[m]> target:
                high=m-1
            if nums[m]<target:
                low=m+1
        if stored == stored2 and occurance !=1:
            return [-1,-1]
        return [stored,stored2]