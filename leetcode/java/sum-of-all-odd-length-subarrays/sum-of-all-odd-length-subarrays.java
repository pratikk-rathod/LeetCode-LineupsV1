class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum=0
        prefix_sum_array=[0]
        ans=0
        for i in arr:
            prefix_sum+=i
            prefix_sum_array.append(prefix_sum)
        

        n=len(arr)

        if n%2==0:
            n-=1
        if n ==1 :
            return prefix_sum_array[-1]
        
        while n >=1:
            
            for i in range(0,len(arr)):

                print(i)
                if i + n >len(arr):
                   
                    break
                ans+= prefix_sum_array[i+n]
                ans -= prefix_sum_array[i]
            
            n-=2
        return ans
