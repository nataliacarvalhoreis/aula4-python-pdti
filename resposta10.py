# Faça um algoritmo que leia dois vetores com 10 elementos cada. Gere um
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos
# pelos elementos intercalados dos dois outros vetores.

vet1 = []
vet2 = []

print("Informe o vetor 1: ")
for i in range(10):
    vet1.append(int(input("Informe o {}º número: ".format(i+1))))

print("Informe o vetor 2: ")
for i in range(10):
    vet2.append(int(input("Informe o {}º número: ".format(i+1))))

vet1.extend(vet2)

print("Vetor final: ", vet1)