class Solution:
    def findComplement(self, num: int) -> int:
        result=0
        pow=1
        while(num>0):
            result+=(num%2^1)*pow
            pow=pow<<1
            num>>=1
        return result
