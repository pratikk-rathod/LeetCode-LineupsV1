class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        #binary SEarch
        l, r = 0, len(arr)-1
        if arr[r] == len(arr):
            return r +k+1

        def bForMissing(arr, l ,r, k):
            m = l + (r-l)//2
            # print("here is the values of l,r ",l, r,m)
            # print(arr[:m], "upto m", arr[m]-1, len(arr[:m]))
            if l>=r:
                if k< arr[l] and k + len(arr[:l]) <arr[l]:
                    # print("coming here")
                    return len(arr[:l])+k
                else:
                    return arr[l] + (k - (arr[l] -len(arr[:l]))) +1
                # return l +k +1
            
            if len(arr[:m]) == arr[m]-1:
                l=m+1
                # print('midddddddddd')
                return bForMissing(arr,l,r,k)
            
            if len(arr[:m]) < arr[m] -1 and k + len(arr[:m])+1 <= arr[m]:
                r=m
                # print("inf fffffff")                
                return bForMissing(arr,l,r,k)
            else:
                l=m+1
                # print("in else")
                return bForMissing(arr,l,r,k)

        return bForMissing(arr,l,r,k)



        # count=0
        # curr=arr[0]
        # curri=0
        # for i in range(1,arr[-1]+100000):
        #     if curri>=len(arr):
        #         break
        #     if i == arr[curri]:
        #         curri+=1
        #         continue
        #     if i !=arr[curri]:
        #         count+=1 
        #     if count == k:
        #         return i
            
        # ans=arr[-1]     
        # while count<k:
        #     count+=1
        #     ans+=1
        # return ans        

        # # Brute Force

        # # array=sorted(list(set([i for i in range(1,arr[-1]+10000)]) - set(arr)))
        # # return array[k-1]