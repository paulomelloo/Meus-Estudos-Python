"""
Crie 3 tabelas com o nome, idade e status (aprovado ou reprovado)
Repetição: Use um loop for para percorrer cada linha (sublista) em tabela_alunos.
Ação: Dentro do loop, acesse os elementos da linha usando a indexação ([0], [1], [2]) e imprima a informação na seguinte ordem:
"""

aluno1 = ["alice", 25, "aprovada"]
aluno2 = ["bruno", 19, "reprovado"]
aluno3 = ["joao", 22, "aprovado"]

alunos = [aluno1, aluno2, aluno3]
print(alunos)

for tabela_alunos in alunos:
    nome = tabela_alunos[0]
    idade = tabela_alunos[1]
    status = tabela_alunos[2]
    print(f"{nome}, tem {idade} anos e foi {status}")