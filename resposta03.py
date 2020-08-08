# Faça um algoritmo que leia 4 notas, mostre as notas e a média na tela.

notas = []
soma = 0

for i in range(4):
    notas.append(float(input("Informe a {}ª nota: ".format(i+1))))
    soma += notas[i]

print("Notas digitadas: ", notas)

media = soma/4
print("A média das notas é: ", media)