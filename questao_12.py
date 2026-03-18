alunos = []
for i in range(3):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    
    notas = []
    for j in range(3):
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
    
    aluno = {
        "nome": nome,
        "idade": idade,
        "notas": notas
    }
    
    alunos.append(aluno)

print("\nMédias dos alunos:")
for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f"Aluno: {aluno['nome']} - Média: {media:.2f}")