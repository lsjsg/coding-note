class Solution:
    """
    计算数字k在0到n中的出现的次数，k可能是0~9的一个值
    例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，
    我们发现1出现了5次 (1, 10, 11, 12)
    An integer denote the count of digit k in 1..n
    """
    def digitCount(self,k,n):
        count = 0
        for i in range(n+1):
            if str(k) in str(i):
                count += 1
        return count
if __name__=="__main__":
    test = Solution()
    print(test.digitCount(1,12))
