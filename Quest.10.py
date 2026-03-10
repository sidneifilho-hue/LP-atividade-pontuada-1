import os

os.system("cls||clear")

litros = float(input(" digite o númeor de litros:"))
tipo_combustivel = input(" digite o tipo de combustivel, A ou G: ")

if tipo_combustivel == "A":
    preço = 3.79
elif tipo_combustivel == "G":
    preço = 6.59
    
total = litros * preço
print("valor a pagar:", total)

