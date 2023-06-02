"""
python实现电子技术门电路与芯片
2023/6/1
"""


def AND(a, b, c=1, d=1):
    """
    :param d:
    :param c:
    :param a:
    :param b:
    :return:  与门
    """
    ac = a and c
    bd = b and d
    return ac and bd


def OR(a, b):
    """
    :param a:
    :param b:
    :return:  或门
    """
    return a or b


def NOT(a):
    """
    :param a:
    :return:  非门
    """
    if a == 1:
        return 0
    else:
        return 1


def AND_NOT(a, b):
    """
    :param a:
    :param b:
    :return:   与非门
    """
    c = AND(a, b)
    return NOT(c)


def OR_NOT(a, b):
    """
    :param a:
    :param b:
    :return:  或非门
    """
    c = OR(a, b)
    return NOT(c)


def XOR(a, b):
    """
    :param a:  0 or 1
    :param b:  0 or 1
    :return:   异或门
    """
    fa = NOT(a)
    fb = NOT(b)
    return OR(AND(a, fb), AND(fa, b))


def XNOR(a, b):
    """
    :param a:  0 or 1
    :param b:  0 or 1
    :return:   同或门
    """
    c = XOR(a, b)
    return NOT(c)
