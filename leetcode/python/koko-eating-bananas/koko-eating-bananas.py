class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles)==h:
        #     return max(piles)
        # if len(piles)==1:
        #     return 2
        minn,maxx= 1, max(piles)

        while minn<maxx:

            mid = minn + (maxx -minn)//2

            ans=0

            for i in piles:
                temp=i//mid
                temp_rem = i% mid

                if temp==0 and temp_rem!=0:
                    ans+=1
                elif temp!=0 and temp_rem!=0:
                    ans+= temp+1
                elif temp!=0 and temp_rem==0:
                    print("here")
                    ans+= temp
                # print("temp",temp)
                # if temp == int(temp):
                #     ans+= int(temp)
                # if temp> int(temp):
                #     ans+=int(temp)+1
            # print(minn, maxx, mid , ans )
            print(ans)
            if ans < h:
                maxx=mid
            elif ans> h:
                minn=mid+1
            elif ans==h:
                maxx=mid
        return minn

    #     # return sum(piles)
    #     class Solution:
    # # import math

    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     minn=1
    #     maxx=max(piles)
    #     def isSufficientSpeed(cnt):
    #         temp=0
    #         for k in piles:
    #             temp+=ceil(k/cnt)
    #         return  temp<=h
        
    #     while minn<maxx:
    #         m=(minn+maxx)//2
    #         if isSufficientSpeed(m):
    #             maxx=m
    #         else:
    #             minn=m+1
            
                
            

    #     return minn