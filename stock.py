import random

n = 4
dados = [random.randint(1, 6) for _ in range(n)]
dados_sum = sum(dados)
print(dados_sum)


def danoFinal(modValor,  talentos, habClass):
    danoExtra = modValor + talentos + habClass
    return danoExtra + dados_sum


danoDisplay = danoFinal

crit = True
print("dano: ", danoDisplay)

if crit is True:
    modDeCrit = 4
    danoCrit = danoDisplay * modDeCrit
    print("Critico: ", danoCrit)
