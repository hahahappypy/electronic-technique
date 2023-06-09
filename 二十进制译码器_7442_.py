"""
7442 二-十进制译码器，输入0000~1001的8421BCD码，输出对应的十进制数
6/2
"""

from 基本门电路 import AND_NOT, NOT


class _7442_:
    def Y0(self, A0, A1, A2, A3):
        return AND_NOT(NOT(A0), NOT(A1), NOT(A2), NOT(A3))  # 0000  0

    def Y1(self, A0, A1, A2, A3):
        return AND_NOT(A0, NOT(A1), NOT(A2), NOT(A3))  # 0001  1

    def Y2(self, A0, A1, A2, A3):
        return AND_NOT(NOT(A0), A1, NOT(A2), NOT(A3))  # 0010  2

    def Y3(self, A0, A1, A2, A3):
        return AND_NOT(A0, A1, NOT(A2), NOT(A3))  # 0011  3

    def Y4(self, A0, A1, A2, A3):
        return AND_NOT(NOT(A0), NOT(A1), A2, NOT(A3))  # 0100  4

    def Y5(self, A0, A1, A2, A3):
        return AND_NOT(A0, NOT(A1), A2, NOT(A3))  # 0101  5

    def Y6(self, A0, A1, A2, A3):
        return AND_NOT(NOT(A0), A1, A2, NOT(A3))  # 0110  6

    def Y7(self, A0, A1, A2, A3):
        return AND_NOT(A0, A1, A2, NOT(A3))  # 0111  7

    def Y8(self, A0, A1, A2, A3):
        return AND_NOT(NOT(A0), NOT(A1), NOT(A2), A3)  # 1000  8

    def Y9(self, A0, A1, A2, A3):
        return AND_NOT(A0, NOT(A1), NOT(A2), A3)  # 1001 9


def two2ten(A, B, C, D):
    """
    利用7442将2进制转化为10进制
    """
    sb = _7442_()
    if sb.Y0(A, B, C, D) == 0: return 0
    if sb.Y1(A, B, C, D) == 0: return 1
    if sb.Y2(A, B, C, D) == 0: return 2
    if sb.Y3(A, B, C, D) == 0: return 3
    if sb.Y4(A, B, C, D) == 0: return 4
    if sb.Y5(A, B, C, D) == 0: return 5
    if sb.Y6(A, B, C, D) == 0: return 6
    if sb.Y7(A, B, C, D) == 0: return 7
    if sb.Y8(A, B, C, D) == 0: return 8
    if sb.Y9(A, B, C, D) == 0: return 9
