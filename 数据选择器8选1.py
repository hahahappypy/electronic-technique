"""
8选1数据选择器
74LS151
G=1输出0
G=0输出Di
"""
from 基本门电路 import AND, NOT

class _74LS151_:
    def __init__(self, G, D0, D1, D2, D3, D4, D5, D6, D7):
        self.G = G
        self.D0 = D0
        self.D1 = D1
        self.D2 = D2
        self.D3 = D3
        self.D4 = D4
        self.D5 = D5
        self.D6 = D6
        self.D7 = D7

    def Y(self, A2, A1, A0):
        cd0 = AND(NOT(A0), NOT(A1), NOT(A2))
        cd1 = AND(A0, NOT(A1), NOT(A2))
        cd2 = AND(NOT(A0), A1, NOT(A2))
        cd3 = AND(NOT(A2), A1, A0)
        cd4 = AND(A0, NOT(A1), NOT(A2))
        cd5 = AND(NOT(A2), A1, NOT(A0))
        cd6 = AND(A2, A1, NOT(A0))
        cd7 = AND(A2, A1, A0)
        y = cd0*self.D0 + cd1*self.D1 + cd2*self.D2 + cd3*self.D3 \
            + cd4*self.D4 + cd5*self.D5 + cd6*self.D6 + cd7*self.D7
        return y*NOT(self.G)