alunos = dict()

for i in range(5):
    nome = input("Digite o nome do aluno {}: ".format(i))
    nota = float(input("Digite a nota de {}: ".format(nome)))
    alunos[nome] = nota

maior = max(alunos, key=alunos.get)
print("Nome: {}. Nota: {}".format(maior, alunos[maior]))