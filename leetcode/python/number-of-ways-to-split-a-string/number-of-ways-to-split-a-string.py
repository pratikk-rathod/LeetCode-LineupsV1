# import math


# class Solution:
#     def numWays(self, s: str) -> int:
#         def binomial(x,k):
#             from math import factorial
#             return factorial(x) // (factorial(k) * factorial(x - k))
#         mod = 10 **9 +7
#         n= len(s)
#         summ=0
#         if s.count("1")>=1:
#             summ=s.count("1")
#         if summ%3 !=0:
#             return 0
#         if summ==0:
#             return binomial(n-1,2) % mod
#         ans=0
        
#         f_l=0
#         f_m=0
#         f_r=0
#         l=0
#         m=0
#         r=0

#         counterr=summ//3
#         tempc=0
#         firstc=0

#         for i in range(len(s)):

#             if s[i]=="1":
#                 tempc+=1
#                 if tempc==1:
#                     if f_l==0 and f_m==0 and f_r==0:
#                         f_l=i
#                     elif f_l!=0 and f_m==0 and f_r ==0:
#                         f_m=i
#                     elif f_l!=0 and f_m!= 0 and f_r==0:
#                         f_r=i
                 
#             firstc=tempc
#             # print(firstc)
#             if firstc==counterr:
#                 tempc=0
#                 if l==0 and m==0:
#                     l=i
#                     continue
#                 if m==0 and r ==0:
#                     m=i
#                     continue

#                 if r==0:
#                     r=i
#                     continue
#         if f_r==0:
#             f_l, f_r = f_r, f_l
#             f_m, f_r = f_r, f_m
#         if r==0:
#             l, r = r,l
#             m,r=r,m
#         print(l,m,r)
#         print(f_l,f_m,f_r)


#         ans = ((f_m - l)* (f_r -m )) % mod
#         return ans

# Enhanced version--->>>>>
# Enhanced version--->>>>>
# Enhanced version--->>>>>
# Enhanced version--->>>>>
# Enhanced version--->>>>>


import math


class Solution:
    def numWays(self, s: str) -> int:
        # def binomial(x,k):
        #     from math import factorial
        #     return factorial(x) // (factorial(k) * factorial(x - k))
        mod = 10 **9 +7
        n= len(s)
        summ=0
        if s.count("1")>=1:
            summ=s.count("1")
        if summ%3 !=0:
            return 0
        if summ==0:
            return ((n-1)*(n-2)//2) % mod
        ans=0
        arr=[i for i,c in enumerate(s) if c=="1"]
        print(arr)
        target= summ//3

        return (arr[target]- arr[target-1]) * (arr[2*target]- arr[2*target-1]) % mod