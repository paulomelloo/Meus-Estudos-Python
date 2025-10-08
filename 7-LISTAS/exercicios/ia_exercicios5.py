"""
Objetivo: Usar um loop aninhado para calcular a média de notas de cada aluno.
Lista Aninhada: Defina a seguinte estrutura:

notas_alunos = [
    ["Maria", [8.0, 7.5, 9.0]],
    ["João", [6.0, 5.5, 7.0]],
    ["Ana", [9.5, 9.0, 10.0]]
]

Repetição Externa: Use um for para iterar sobre cada aluno em notas_alunos.
Acesso à Lista Interna: Dentro do loop, extraia a lista de notas do aluno (ela estará no índice [1] da lista atual).
Cálculo: Use a função sum() e len() do Python para calcular a média da lista de notas.
Resultado: Imprima o nome do aluno e sua média final.
"""

notas_alunos = [
    ["Maria", [8.0, 7.5, 9.0]],
    ["João", [6.0, 5.5, 7.0]],
    ["Ana", [9.5, 9.0, 10.0]]
]

for alunos in notas_alunos:
    nome = alunos[0]
    nota1 = alunos[1][0]
    nota2 = alunos[1][1]
    nota3 = alunos[1][2]
    media = (nota1 + nota2 + nota3) / 3
    print(f"Aluno {nome} esta com a média final {media:.2f}")