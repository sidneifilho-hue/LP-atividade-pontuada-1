import os

os.system("cls||clear")

renda_mensal = ("digite a renda mensal: ")
valor_emprestimo = (" digite o valor do emprestimo: ")
numero_prestacao = (" digite o número de prestação: ")

valor_prestacao = valor_emprestimo/numero_prestacao

if valor_emprestimo <= renda_mensal*10 and valor_prestacao <= renda_mensal*0.3:
    print("emprestimo aprovado")
else:
    print (" emprestimo não aprovado")