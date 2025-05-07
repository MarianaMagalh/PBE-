# exer 1
"""
a = 5.00
b = 8.00
c = 12.00

def dobro(numero):
    return numero * 2

print(f"O dobro do produto de R${a}, é {dobro(a)}\n"
      f"O dobro do produto de R${b}, é {dobro(b)}\n"
      f"O dobro do produto de R${c}, é {dobro(c)}")


# exer 2
lista = ["João", "Maria", "Carlos"]

def bemVinde(nome):
    return print(f"Bem Vinde {nome}!")

for nomes in lista:
    print(bemVinde(nomes))


# exer 3
import random

lista = range(1, 10 + 1)

numeros = random.choice(lista)

def acao(numero):
    if numero % 2 == 0:
        return print("Jogador Avança")
    else:
        return print("Jogador Recua")


print(f"Posição do Dado: {numeros}")
print(acao(numeros))


# exer 4
numeros = [2, 3, 4]

def tabuada(num):
    contador = 0

    for _ in range(10):
        tabuada = num * (contador + 1)
        contador += 1

        print(f"{num} X {contador} = {tabuada}")

for numero in numeros:
    print(tabuada(numero))
"""

# exer 5

idade_cli = [8, 15, 20]

def verificacao(idade):
    if idade >= 18:
        return print("Você tem idade para ver o filme.\nBom filme!")
    else:
        return print("Você não tem idade para ver o filme.\nEscolha outro filme!")

print(verificacao(idade_cli))
