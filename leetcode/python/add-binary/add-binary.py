# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         m = min(len(a),len(b))

#         ans=""
#         carry=0
#         for i in range(1,m+1):
#             print(ans)
#             # carry=0
#             if carry==0:
#                 if int(a[-m])==0 and int(b[-m])==0:
#                     carry=0
#                     ans+='0'
#                     continue

#                 if int(a[-m])==1 and int(b[-m])==1:
#                     carry=1
#                     ans+='0'
#                     continue
                
#                 if int(a[-m])==1 and int(b[-m])==0:
#                     carry=0
#                     ans+='1'
#                     continue

#                 if int(a[-m])==0 and int(b[-m])==1:
#                     carry=0
#                     ans+='1'
#                     continue

            
#             if carry==1:
#                 if int(a[-m])==0 and int(b[-m])==0:
#                     carry=0
#                     ans+='1'
#                     continue

#                 if int(a[-m])==1 and int(b[-m])==1:
#                     carry=1
#                     ans+='1'
#                     continue
                
#                 if int(a[-m])==1 and int(b[-m])==0:
#                     carry=1
#                     ans+='0'
#                     continue

#                 if int(a[-m])==0 and int(b[-m])==1:
#                     carry=1
#                     ans+='0'
#                     continue

        
#         if len(b)==m and len(a)>m:
#             m+=1
#             while m<len(a):
#                     # carry=0
#                 if carry==0:
#                     if int(a[-m])==0 and int(b[-m])==0:
#                         carry=0
#                         ans+='0'
#                         continue


#                     if int(a[-m])==1 and int(b[-m])==1:
#                         carry=1
#                         ans+='0'
#                         continue
                    
#                     if int(a[-m])==1 and int(b[-m])==0:
#                         carry=0
#                         ans+='1'
#                         continue

#                     if int(a[-m])==0 and int(b[-m])==1:
#                         carry=0
#                         ans+='1'
#                         continue
                
#                 if carry==1:
#                     if int(a[-m])==0 and int(b[-m])==0:
#                         carry=0
#                         ans+='1'
#                         continue

#                     if int(a[-m])==1 and int(b[-m])==1:
#                         carry=1
#                         ans+='1'
#                         continue
                    
#                     if int(a[-m])==1 and int(b[-m])==0:
#                         carry=1
#                         ans+='0'
#                         continue

#                     if int(a[-m])==0 and int(b[-m])==1:
#                         carry=1
#                         ans+='0'
#                         continue

                
#                 m+=1
            
#         if len(a)==m and len(b)>m:
                
#             m+=1
#             while m<len(b):
#                     # carry=0
#                 if carry==0:
#                     if int(a[-m])==0 and int(a[-m])==0:
#                         carry=0
#                         ans+='0'

#                     if int(a[-m])==1 and int(a[-m])==1:
#                         carry=1
#                         ans+='0'
                    
#                     if int(a[-m])==1 and int(a[-m])==0:
#                         carry=0
#                         ans+='1'
#                     if int(a[-m])==0 and int(a[-m])==1:
#                         carry=0
#                         ans+='1'
                
#                 if carry==1:
#                     if int(a[-m])==0 and int(a[-m])==0:
#                         carry=0
#                         ans+='1'

#                     if int(a[-m])==1 and int(a[-m])==1:
#                         carry=1
#                         ans+='1'
                    
#                     if int(a[-m])==1 and int(a[-m])==0:
#                         carry=1
#                         ans+='0'
#                     if int(a[-m])==0 and int(a[-m])==1:
#                         carry=1
#                         ans+='0'
                
#                 m+=1

        
#         return ans[::-1]
                
        
            
class Solution:
  
  def addBinary(self, a: str, b: str) -> str:
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(s))
    