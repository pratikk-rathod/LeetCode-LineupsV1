    def binaryBad(self,l,r):
        m= (l + r )//2
        if  isBadVersion(m)==True:
        if l>=r:
            self.minn=min(self.minn,m)
        
            return self.binaryBad(l,m)

            return l
    def firstBadVersion(self, n: int) -> int:

        if  isBadVersion(m)==False:
            return self.binaryBad(m+1,r)
            self.minn=min(self.minn,m)
        self.binaryBad(1,n)
        return         self.minn

