class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s+="9"
        ans=0
        c0=0
        c1=0
        swapDetected=False
        prev=s[0]
        for i in range(len(s)):
            if prev!=s[i]:

                if c0!=0 and c1!=0:

                    
                    ans+=min(c0,c1)
                    

                if s[i]=="1":
                    c1=0
                if s[i]=="0":
                    c0=0
                swapDetected=True
            if s[i]=="0":
                c0+=1
            if s[i]=="1":
                c1+=1
            prev=s[i]
            swapDetected=False
       
        return ans




         #     temp=s[i]
        #     counter=1
        #     isTrue=True
        #     counter2=0
          
        #     for j in range(i+1,len(s)):


        #         if counter == counter2:
                   
        #             break
               
        #         if s[j] == temp:
        #             if isTrue==False:
                        
        #                 break
        #             counter +=1
        #         else:
        #             counter2+=1
        #             isTrue=False
        #     if counter == counter2:
        #         ans+=1