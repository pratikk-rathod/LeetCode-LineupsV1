class Solution:

    # Brute Force #
    
    def minDeletionSize(self, strs: List[str]) -> int:
        prev=strs[0]
        x=len(prev)
        ans=0
        already=[]
        for i in range(1,len(strs)):

            for j in range(x):
                if j in already:
                    continue
                else:
                    if prev[j] > strs[i][j]:
                        ans+=1
                        already.append(j)
            prev= strs[i]
        return ans