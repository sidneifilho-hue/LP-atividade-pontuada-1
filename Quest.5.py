import os

os.system("cls||clear")

A = int(input("Digite um valor para representar A: "))
B = int(input("Digite um valor para representar B: "))

Soma = A+B
Subtracao = A-B
Multiplicacao = A*B
Divisao = A/B

operacao = input("Digite o operador desejado (+,-,*,/):")

if operacao == "+":
    print(" A+B = ",Soma)
elif operacao == "-":
    print(" A-B = ",Subtracao)
elif operacao == "*":
    print(" A*B = ",Multiplicacao)
elif operacao == "/":
    print(" A/B = ",Divisao)
    
