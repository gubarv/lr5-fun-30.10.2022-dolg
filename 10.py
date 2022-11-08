names = ['Маша', 'Петя', 'Вася']

def cd(nn):
    code = list(map(lambda x: hash(x), nn))
    print(code)

cd(names)