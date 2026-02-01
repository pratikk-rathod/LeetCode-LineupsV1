class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        minn=min(bloomDay)
        maxx=max(bloomDay)

        ans=1000000000000 
        tempArray=bloomDay

        def customBS(bloomDay,l,r):
            # print(notlocal ans)
            nonlocal ans
            if r<l:
                return
            tempcounter=0
            tempcounter2=0
            mid= l +(r-l)//2

            for i in range(len(bloomDay)):
                # print("tempcounter", tempcounter, tempcounter2,k)

                if bloomDay[i]<=mid:
                    tempcounter+=1
                    if tempcounter>=k:
                        tempcounter2+=1
                        tempcounter=0


                else:
                    tempcounter=0
            # print(ans, l , r , mid, "ans L R m")

            # print(tempcounter,tempcounter2)
            
            if tempcounter2>=m:
                ans=min(ans,mid)
                r=mid-1
                return customBS(bloomDay,l,r)
            if tempcounter2<m:
                l=mid+1
                return customBS(bloomDay,l,r)
        
        customBS(bloomDay,minn,maxx)
        if ans==1000000000000:
            return -1
        
        return ans