n = int(input('Введите систему счисления: '))
c = int(input('Введите число: '))
b = ''

def ch(arg_c, arg_b, arg_n):
    while arg_c > 0:
        arg_b = str(arg_c % arg_n) + arg_b
        arg_c = arg_c // arg_n
    print(arg_b)

ch(c, b, n)