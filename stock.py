import random

n = 4 #number of dices to roll
dados = [random.randint(1, 6) for _ in range(n)] #Edit as damage changes
dados_sum = sum(dados)
print(dados_sum)


def danoFinal(modValor,  talentos, habClass):
    danoExtra = modValor + talentos + habClass
    return danoExtra + dados_sum


danoDisplay = danoFinal(10, 3, 2) #Edit as your Char progress

crit = True
print("dano: ", danoDisplay)

if crit is True:
    modDeCrit = 4 #Edit as weapon crit damage changes
    danoCrit = danoDisplay * modDeCrit
    print("Critico: ", danoCrit)
