class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        counter=0
        isIncreasing=True
        isDecreasing=True

        Firstcheck=False
        prev=nums[0]
        # val=nums[1]
        # if val<prev:
        #     return False
        for key,val in enumerate(nums[1:]):
            if val==prev:
                return False
            # print(val,key)
            if counter>3:
                return False
            
            if val>prev:
                if isDecreasing == True:
                    counter+=1
                isIncreasing=True
                isDecreasing=False
                
                Firstcheck=True
            

            if Firstcheck==True:
                if val<prev:
                    if isIncreasing == True:
                        counter+=1
                    isIncreasing=False
                    isDecreasing=True
            else:
                return False
            prev=val

            
        return True if counter==3 else False
            
