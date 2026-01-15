# 35 mines
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        def customm(nums,l,r):

            m=l+(r-l)//2
            print(l,m,r,"l m r")
            if r<l:
                return nums[l]
            if m!=0 and m<len(nums)-1:
                if nums[m-1] == nums[m]:
                    if (m-l-1) %2 !=0:
                        print("insided if if")
                        return customm(nums,l,m-2)
                    else:
                        print("insided if else")
                        return customm(nums,m+1,r)
                elif nums[m+1] == nums[m]:
                    if (m-l-1) %2 !=0:
                        print("insided elif if")
                        return customm(nums,m+2,r)
                    else:
                        print("insided elif else")
                        return customm(nums,l,m-1)
                
                else:
                    print("i should be here")
                    return nums[m]

            return nums[r]

        l,r = 0, len(nums)-1

        return customm(nums,l,r)
        # a=list(set(nums))

        # for i in a:
        #     if nums.count(i)==1:
        #         return i

        