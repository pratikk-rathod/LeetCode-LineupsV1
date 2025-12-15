class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # print(len(prices))
        if len(prices)==1:
            return 1
        if len(prices)==2:
            return 3 if prices[0]-1 == prices[1] else 2
        prices.append(0)
        prices.append(0)
        # prices.append(0)

        n=len(prices)
        if n==1:
            return 1
        dp=[0] * (n)
        temp=1
        # prev_val=prices[0]
        # curr_val=prices[1]
        for i in range(1,n):

            curr_val=prices[i]
            prev_val= prices[i-1]

            if curr_val +1 == prev_val:
                temp+=1
                continue
            else:
                print("here in temp")
                dp[i]= temp
                temp=1
        # if prices[-]
        # print(dp)


        # ans=n

        # for i in range(n):
        #     x=prices[i]
        #     for j in range(i+1,n):

        #         if x-1 == prices[j]:
        #             x=prices[j]
        #             ans+=1
        #         else:
        #             break\
        # print(dp[-1])
        isvalid =False
        if dp[-1]-1 == n -2:
            print("its true")
            isvalid=True
            # return sum(dp)
        for i, c in enumerate(dp):
            dp[i] = (dp[i]-1) * dp[i] //2
        # print("updated dp", dp        )

        if isvalid:
            return sum(dp)
        return n+ sum(dp) -2