"""
芯片_74138_
"""
from 基本门电路 import AND, AND_NOT, OR, OR_NOT, NOT, XOR, XNOR


class _741387_:

    def __init__(self, G1=1, G2A=0, G2B=0):
        self.G1 = G1
        self.G2A = G2A
        self.G2B = G2B

    def Y0(self, A, B, C, G1=1, G2A=0, G2B=0):
        return NOT(AND(NOT(A), NOT(B), NOT(C), AND(G1, NOT(G2A), NOT(G2B))))

    def Y1(self, A, B, C, G1=1, G2A=0, G2B=0):
        return NOT(AND(A, NOT(B), NOT(C), AND(G1, NOT(G2A), NOT(G2B))))

    def Y2(self, A, B, C, G1=1, G2A=0, G2B=0):
        return NOT(AND(NOT(A), B, NOT(C), AND(G1, NOT(G2A), NOT(G2B))))

    def Y3(self, A, B, C, G1=1, G2A=0, G2B=0):
        return NOT(AND(A, B, NOT(C), AND(G1, NOT(G2A), NOT(G2B))))

    def Y4(self, A, B, C, G1=1, G2A=0, G2B=0):
        return NOT(AND(NOT(A), NOT(B), C, AND(G1, NOT(G2A), NOT(G2B))))

    def Y5(self, A, B, C, G1=1, G2A=0, G2B=0):
        return NOT(AND(A, NOT(B), C, AND(G1, NOT(G2A), NOT(G2B))))

    def Y6(self, A, B, C, G1=1, G2A=0, G2B=0):
        return NOT(AND(NOT(A), B, C, AND(G1, NOT(G2A), NOT(G2B))))

    def Y7(self, A, B, C, G1=1, G2A=0, G2B=0):
        return NOT(AND(A, B, C, AND(G1, NOT(G2A), NOT(G2B))))
