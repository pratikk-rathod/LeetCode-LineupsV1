class Solution:
    def mySqrt(self, x: int) -> int:

        def binary(l,r,target):
            if x==0:    return 0
            if x==1 : return 1
            if r<l :
                return l-1
            m = (l+r) // 2

            if m == target//m:
                return m

            if m >target/m :
                r=m-1
                return binary(l,r,target)
            if m< target/m:
                l=m+1
                return binary(l,r,target)
        

        # ans= 

        return binary(0, x,x)
        