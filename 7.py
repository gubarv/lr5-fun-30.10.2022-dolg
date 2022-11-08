import sympy

n = int(input("Введите число: "))

def pr(arg_n):
    if sympy.isprime(arg_n):
        print(f"Число {arg_n} простое")
    else:
        print(f"Число {arg_n} не простое")

pr(n)