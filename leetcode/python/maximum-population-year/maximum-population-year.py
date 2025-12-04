class Solution:
    def maximumPopulation(self, logs):

        calendar={}
        min_year=logs[0][0]
        max_year=logs[0][1]

        for i in logs:
            if i[0] in calendar: calendar[i[0]] +=1 
            else: calendar[i[0]]=1
            if i[1] in calendar: calendar[i[1]]-=1 
            else: calendar[i[1]]=-1




            if i[0]<min_year : min_year = i[0]
            if i[1]>max_year : max_year = i[1] -1

       
        final_ans=logs[0][0]
        final_ans_index=0
        max_counter=0

        prefix_sum=[]
        best=0
        year=0
        curr=0
        for i in range(min_year, max_year+1):
            if i in calendar:
                curr += calendar[i]
                
                if curr> best:
                    best = curr

                    year= i

        return year