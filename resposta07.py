# Faça um algoritmo que leia um vetor de 5 números inteiros, mostre a
# soma, a multiplicação e os números.

numeros = []
soma = 0
mult = 1

for i in range(5):
    numeros.append(int(input("Informe o {}º numero: ".format(i+1))))
    mult *= numeros[i]
    soma += numeros[i]

print("Números lidos: ", numeros)


print("\nSoma dos números: ", soma)
print("Multiplicação dos números: ", mult)