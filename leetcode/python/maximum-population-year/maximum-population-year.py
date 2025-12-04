class Solution:
    def maximumPopulation(self, logs):

        calendar={}
        min_year=1950
        max_year=2050
        arr = [0] * 102

        for i in logs:
            arr[i[0] - 1950 ] +=1
            arr[i[1] - 1950] -=1
        
        ans=0
        best=0
        curr=0
        for i in range(len(arr)):
            
            curr+=arr[i]

            if curr>best:
                best=curr
                ans=1950+i
            
        return ans


    #     class Solution:
    # def maximumPopulation(self, logs):

    #     calendar={}
    #     min_year=999999
    #     max_year=-9999999

    #     for i in logs:
    #         if i[0] in calendar: calendar[i[0]] +=1 
    #         else: calendar[i[0]]=1
    #         if i[1] in calendar: calendar[i[1]]-=1 
    #         else: calendar[i[1]]=-1




    #         if i[0]<min_year : min_year = i[0]
    #         if i[1]>max_year : max_year = i[1] -1

    #         # for j in range(i[0],i[1]):

    #         #     if j in calendar:
    #         #         calendar[j]+=1
    #         #     else:
    #         #         calendar[j]=1
       
    #     final_ans=logs[0][0]
    #     final_ans_index=0
    #     max_counter=0
    #     print(calendar)
    #     print(min_year)
    #     print(max_year)
    #     prefix_sum=[]
    #     summ=0
    #     best=0
    #     index=0
    #     year=0
    #     curr=0
    #     for i in range(min_year, max_year+1):
    #         if i in calendar:
    #             curr += calendar[i]
                
    #             if curr> best:
    #                 best = curr

    #                 year= i

    #     return year