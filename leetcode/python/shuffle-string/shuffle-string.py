class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        arr= [0] * n

        for i in range(n):
            arr[indices[i]] = s[i]

        x="".join(arr)
        
        return x