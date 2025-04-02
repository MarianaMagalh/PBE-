# exer 1
'''
num = int(input("Insira um número: "))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} não é par.")
'''

# exer 2
'''
num =  int(input("Insira um número: "))

if num > 10:
    print(f"O número {num} é maior que 10.")
else:
    print(f"O número {num} não é maior que 10.")
'''

# exer 3
'''
idade = int(input("Insira a sua idade: "))

if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Parece que você não é maior de idade.")
'''

# exer 4
'''
idade = int(input("Qual a sua idade: "))

if idade < 16:
    print("Voto não obrigatorio. Você ainda não tem idade para votar!")
elif idade >= 60:
    print("Voto Opcional. Não há a necessidade de voto.")
else:
    print("Voto obrigatório.")
'''

# exer 5
'''
num = int(input("Insira o número: "))

if num == 0:
    print(f"O número é {num}")
elif num >= 0:
    print("O numero é positivo!")
else:
    print("O número é negativo")
'''

# exer 6
'''
nota = int(input("Insira a nota do aluno: "))

if nota >= 9:
    print("A")
elif nota == 7:
    print("B")
elif nota >= 5:
    print("C")
elif nota >= 3:
    print("D")
else:
    print("E")
'''

# exer 7
'''
idade =  int(input("Informe a sua idade, para saber de tem direito a desconto:"))

if idade >= 18 and idade <= 60:
    print("Você não tem direito a desconto.")
else:
    print("Você tem direito a desconto")
'''

# exer 8
'''
lad1 = int(input("Insira o tamanho de um dos lados do possivel triangulo: "))
lad2 = int(input("Insira o tamanho de um dos lados do possivel triangulo: "))
base = int(input("Insira o tamanho da base do possivel triangulo: "))


if (lad1 + lad2) >= base:
    print("É um triangulo")
    if lad1 == lad2 and lad2 == base and base == lad1:
        print("Triangulo equilátero")
    elif lad1 == lad2 and lad1 != base:
        print("Triangulo isósceles")
    else:
        print("Triangulo escaleno")
elif (lad2 + base) >= lad1:
    print("É um triangulo")
    if lad1 == lad2 and lad2 == base and base == lad1:
        print("Triangulo equilátero")
    elif lad1 != lad2 and lad1 != base and lad2 != base:
        print("Triangulo escaleno")
    else:
        print("Triangulo isosceles")
elif (lad1 + base) >= lad2:
    print("É um triangulo")
    if lad1 == lad2 and lad2 == base and base == lad1:
        print("Triangulo equilátero")
    elif lad1 == lad2 and lad1 != base:
        print("Triangulo isósceles")
    else:
        print("Triangulo escaleno")
else:
    print("Não é um triangulo")
'''

# exer 9
'''
valor = int(input("Qual o valor da compra? "))

if valor < 100:
    desconto = valor * (5/100)
    print(f"Você recebeu o desconto de 5%. O valor da sua compra é de R${desconto}")
elif valor >= 100 and valor <= 500:
    desconto = valor * (10/100)
    print(f"Você recebeu o desconto de 10%. O valor total da compra é R${desconto}")
else:
    desconto = valor * (15/100)
    print(f"Você recebeu o desconto de 15%. O valor total da compra é R${desconto}")
'''

# exer 10
'''
ano = int(input("Insira um ano: "))

if ano % 4 == 0 or ano % 400 == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")

'''

# exer 11
'''
altura = float(input("Insira a sua altura: "))
peso =  float(input("Insira o seu peso: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print("Abaixo do peso.")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal.")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso.")
else:
    print("Obesidade.")

'''

# exer 12
'''
num1 = int(input("Insira um número: "))
num2 = int(input("Insira um outro número: "))
num3 = int(input("Insira mais um número: "))

if num1 == num2 and num2 == num3 and num3 == num1:
    print("São iguais.")
elif num1 < num2 and num1 < num3 and num2 < num3:
    print("Crescente.")
elif num1 > num2 and num2 > num3 and num1 > num3:
    print("Decrescente.")
else:
    print("numeros invalidos")
'''

# exer 13
'''
temC = float(input("Insira a temperantura atual: "))

if temC < 10:
    print("Frio")
elif temC >= 10 and temC < 25:
    print("Aconchegante")
elif temC >= 25 and temC < 40:
    print("Quente")
else:
    print("Muito Quente")
'''

# exer 14
'''
from datetime import datetime

data = input("Insira a sua data de nascimento, ex [d/m/A]: ")

data2 = datetime.strptime(data, "%d/%m/%Y")
print(data2)
'''
