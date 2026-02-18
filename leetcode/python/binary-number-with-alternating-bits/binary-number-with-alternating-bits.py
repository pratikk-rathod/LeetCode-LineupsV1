class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x=bin(n)[2:]


        # x=True
        temp=x[0]
        for i in range(1,len(x)):
            if x[i] == temp:
                return False
            else:
                temp=x[i]
        return True




        