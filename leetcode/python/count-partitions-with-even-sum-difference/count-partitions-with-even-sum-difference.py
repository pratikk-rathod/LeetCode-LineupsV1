class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        prefix_sum=[]
        summ=0

        for i in nums:
            summ+=i
            prefix_sum.append(summ)
        print(prefix_sum)
        ans=0
        for i in range(len(prefix_sum) -1):
            if (2 * prefix_sum[i] - prefix_sum[-1]) %2 ==0:
                ans+=1
        return ans