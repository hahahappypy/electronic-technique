"""
电路实验室
"""
from 二十进制译码器_7442_ import two2ten


def lighta():
    stra = ' ---- '
    print(stra)


def lightb():
    str_b = '\t |\n\t |'
    print(str_b)


def lightbf():
    str_bf = '|\t |\n|\t |'
    print(str_bf)


def lightg():
    str_g = ' ----'
    print(str_g)


def lightc():
    str_c = '\t |\n\t |'
    print(str_c)


def lighte():
    str_e = '|\n|'
    print(str_e)


def lightf():
    str_f = '|\n|'
    print(str_f)


def lightce():
    str_ce = '|\t |\n|\t |'
    print(str_ce)


def lightd():
    str_d = ' ----'
    print(str_d)


def digital_number(D, C, B, A):
    number = two2ten(A, B, C, D)
    match number:
        case 0:
            lighta()
            lightbf()
            lightce()
            lightd()
        case 1:
            lightb()
            lightc()
        case 2:
            lighta()
            lightb()
            lightg()
            lighte()
            lightd()
        case 3:
            lighta()
            lightb()
            lightg()
            lightc()
            lightd()
        case 4:
            lightbf()
            lightg()
            lightc()
        case 5:
            lighta()
            lightf()
            lightg()
            lightc()
            lightd()
        case 6:
            lighta()
            lightf()
            lightg()
            lightce()
            lightd()
        case 7:
            lighta()
            lightb()
            lightc()
        case 8:
            lighta()
            lightbf()
            lightg()
            lightce()
            lightd()
        case 9:
            lighta()
            lightbf()
            lightg()
            lightc()
            lightd()






