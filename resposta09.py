# Faça um algoritmo que leia um vetor A com 10 números inteiros, calcule e
# mostre a soma dos quadrados dos elementos do vetor.

vetor = []
soma = 0
quadrado = 0

for i in range(10):
    vetor.append(int(input("Informe o {}º número: ".format(i+1))))
    quadrado = vetor[i]*vetor[i]
    soma += quadrado

print("Vetor digitado: ", vetor)
print("Soma dos quadrados: ", soma)