# Faça um algoritmo que leia um vetor de 10 caracteres, e diga quantas
# consoantes foram lidas. Imprima as consoantes.

vetor = []
consoantes = []

for i in range(10):
    vetor.append(input("Informe a letra: "))

for letra in vetor:
    if "aeiou".find(letra) == -1:
        consoantes.append(letra)

print(consoantes)