import os

os.system("cls||clear")

nome= input("Digite o nome do produto: ")
quantidade_adquirida = (" Digite a quantidade adquirida: ")
preco_unitario = (" Digite o preço unitário:")

total = quantidade_adquirida * preco_unitario

if quantidade_adquirida <= 5:
    desconto == total * 0.02
    
elif quantidade_adquirida <= 10:
    desconto == total * 0.03
else:
    desconto == total * 0.05
    

total_pagar = total - desconto 
print(nome)
print(quantidade_adquirida)
print(preco_unitario)
print (total_pagar)