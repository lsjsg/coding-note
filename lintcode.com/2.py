import time
t1=time.time()
class Solution:
    """
    设计一个算法，计算出n阶乘中尾部零的个数
    An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self,n):
        sum = 0
        while(n>5):
            n = int(n / 5)
            sum += n
        return sum

if __name__=="__main__":
    test = Solution()
    t2=time.time()
