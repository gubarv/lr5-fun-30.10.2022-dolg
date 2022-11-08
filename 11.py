from functools import reduce

sentences = ['научиться плести рыболовные сети',
             'обучать нейронные сети',
             'паук ловит в сети мух']


def pd(sen):
    podch = reduce(lambda a, x: a + x.count('сети'), sen, 0)
    print(podch)

pd(sentences)