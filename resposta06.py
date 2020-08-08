# Faça um algoritmo que peça as quatro notas de 10 alunos, calcule e
# armazene num vetor a média de cada aluno, imprima o número de alunos
# com média maior ou igual a 7.0.

medias = []
soma = 0
media = 0
nota = 0
cont = 0

for i in range(3):
    print("Informe as notas do aluno {}: ".format(i+1))
    for j in range(4):
        nota=float(input("Informe a {}ª nota: ".format(i+1)))
        soma += nota
    media = soma/4
    if media >= 7.0:
        cont+=1
    medias.append(media)
    soma = 0

print("Médias dos alunos: ", medias)

print("\nAlunos com média acima de 7.0: ", cont)
