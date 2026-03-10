import os

os.system("cls||clear")

A = int(input("Digite um valor para representar A: "))
B = int(input("Digite um valor para representar B: "))
C = int(input("Digite um valor para representar C: "))

soma = A + B 

if soma < C:
    print (" A + B é menor que C ")
elif soma == C:
    print(" A + B é igual a C ")
else:
    print (" A + B é maior que C")