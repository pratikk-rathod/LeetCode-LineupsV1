class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if len(arr)==1 and arr[0] !=1 and k==1 :
            return 1

        count=0
        # prev=
        curr=arr[0]
        curri=0
        for i in range(1,arr[-1]+100000):
            if curri>=len(arr):
                break
            if i == arr[curri]:
                curri+=1

                continue
            if i !=arr[curri]:
                count+=1 
            if count == k:
                return i
            
        ans=arr[-1]     
        while count<k:
            count+=1
            ans+=1
        return ans        


            
    
        # Brute FOrce

            # # print(arr)
            # array=sorted(list(set([i for i in range(1,arr[-1]+10000)]) - set(arr)))

            # return array[k-1]