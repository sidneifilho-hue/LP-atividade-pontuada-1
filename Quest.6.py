import os

os.system("cls||clear")

n1 = float(input(" Digite a primeira nota:"))
n2 = float(input(" Digite a segunda nota:"))

media = (n1 + n2)/2
print (media)

if media >= 6:
    print("Parabéns, você esta aprovado")
elif media >= 4:
    print(" Está de recuperanção ")
else:
    print (" Reprovado ")