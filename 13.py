names = ['Саша', 'Даша', 'Паша', 'Петя']
ballmath = [20, 80, 100, 91]
ballrus = [33, 76, 89, 84]
ballinf = [40, 90, 100, 75]

def bl(n, bm, br, bi):
    res = list(zip(n, bm, br, bi))
    print(res)

bl(names, ballmath, ballrus, ballinf)