
#     &                         <<  左移一位                 >>   右移一位
#   101010   (n)                相当于乘上进制                相当于除以进制
# & 000001   (1)                  1010                        10100
# ---------                      10100                         1010
#   000000   (结果)

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res