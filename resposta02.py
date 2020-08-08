# Faça um algoritmo que leia um vetor de 10 números reais e mostre-os na
# ordem inversa.

numeros = []

for i in range(10):
    numeros.append(float(input("Informe o {}º numero: ".format(i+1))))

for itens in reversed(numeros):
    print(itens)