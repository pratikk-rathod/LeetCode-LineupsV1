class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low,high= 0, len(nums)-1
        arr=nums
        def binarySearchModified(l,r, target):
            # print("fata")
            print(l,r)
            if l>r:
                return -1
            mid = l+(r-l)//2

            if nums[mid] == target:
                return mid
            
            if nums[l]<=nums[mid]:
                if target>= nums[l] and target<nums[mid]:
                    r=mid-1
                    return binarySearchModified(l,r,target)
                else:
                    l=mid+1
                    return binarySearchModified(l,r,target)
            else:
                if target>nums[mid] and target<=nums[r]:
                    l=mid+1
                    return binarySearchModified(l,r,target)
                else:
                    r=mid-1
                    return binarySearchModified(l,r,target)

            # if arr[l]>arr[mid] or arr[l]>arr[r]:
            #     if arr[l]== target:
            #         return l
            #     else:
            #         return binarySearchModified(l+1,r, target)
            
            # else:
            #     if arr[mid] == target:
            #         return mid
                
            #     if arr[mid]>target:
            #         return binarySearchModified(l,mid-1, target)

            #     if arr[mid]<target:
            #         return binarySearchModified(l+1,r, target)

        ans= binarySearchModified(low,high, target)
        print(ans)
        return binarySearchModified(low,high, target)