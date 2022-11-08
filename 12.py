l = []
n = int(input())

def lr(arg_n):
    for i in range(n):
        l.append(int(input()))

def ch(li):
    l1 = list(filter(lambda x: x % 7 == 0, li))
    if l1 == []:
        print('Числе кратных 7 нет')
    else:
        print(l1)
lr(n)
ch(l)