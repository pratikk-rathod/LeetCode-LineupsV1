#BRUTE FORCE
class Solution:
    def reverseBits(self, n: int) -> int:

        ans = (bin(n)[:1:-1])

        x=32 - len(ans)
        print(ans)

        q=""
        for i in range(x):
            q+="0"
        return int(str((bin(n)[:1:-1])+q),2)
        