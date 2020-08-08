# Faça um algoritmo que peça a idade e a altura de 5 pessoas, armazene
# cada informação no seu respectivo vetor. Imprima a idade e a altura na
# ordem inversa a ordem lida

idades = []
alturas = []
for i in range(5):
    idades.append(int(input("Informe a idade {}:  ".format(i+1))))
    alturas.append(float(input("Informe a altura {}: ".format(i+1))))

#invertendo as listas
alturas.reverse()
idades.reverse()

print("alturas:", alturas)
print("idades:",  idades)
