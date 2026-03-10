import os

os.system("cls||clear")

preco_morango = 2.50
preco_macas = 1.80

quantidade_morangos = int(input(" Digite a quantidade de morangos: "))
quantidade_macas = int(input(" Digite a quantidade de macas: "))

total_frutas = quantidade_morangos + quantidade_macas

valor_total = (quantidade_macas * preco_macas)+(quantidade_morangos*preco_morango)

if total_frutas >= 10 or valor_total > 15:
    valor_total == valor_total*0.9
else:
    print(" valor a pagar:", valor_total)