# class Solution:
#     def bestClosingTime(self, customers: str) -> int:
#         lem=len(customers)
#         penalties={}
#         counter=0

#         for i in range(len(customers)+1):
#             penalty=0
#             if i==0:
#                 for j in customers:
#                     if j=="Y":
#                         penalty+=1
#                 penalties[0]=penalty
#                 continue            
#             else:
                    
#                 for j in range(len(customers)):
                    
#                     if counter<j:
#                         if customers[j]=="Y":
#                             penalty+=1
#                     if counter>j:
#                         if customers[j]=="N":
#                             penalty+=1
#                     if counter==j:
#                         if customers[j]=="N":
#                             penalty+=1
#                 penalties[i]=penalty
#                 counter+=1

#         # print(penalties)
#         maxx=min(penalties.values())
#         for key,value in penalties.items():
#             if value==maxx:
#                 return key

#         # return maxx
#         # return maxx
#         # return maxx
#         # return maxx
#         # return maxx
#         # return maxx
#         # return maxx
        

class Solution:
    def bestClosingTime(self, cust: str) -> int:
        
        x = y = z = 0
        for i, charr in enumerate(cust):     
            z += (charr == "Y") * 2 - 1       
            if z > y:                       
                y, x = z, i+1               
        return x