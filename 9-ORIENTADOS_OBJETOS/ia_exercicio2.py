"""
Criar uma classe que rastreia o progresso de leitura de um livro, usando lógica condicional (if/elif/else) dentro de um método.
1- Crie uma Classe chamada Livro.
2- Defina o método construtor (__init__) que recebe e inicializa:
    titulo
    autor
    paginas_total (o número total de páginas)
    Defina um atributo interno chamado paginas_lidas, inicializando-o com 0.
3- Crie um Método chamado ler(quantidade_paginas) que adiciona o valor de quantidade_paginas ao atributo paginas_lidas.
4- Crie um Método chamado verificar_progresso() que retorna uma string descrevendo o status atual da leitura:
    Se paginas_lidas for igual a paginas_total, retorne: "Parabéns! Livro concluído."
    Caso contrário, retorne: "Progresso: X páginas de Y páginas lidas."
5- Crie um Objeto Livro e use o método ler() algumas vezes.
6- Use o print() no resultado do método verificar_progresso().
"""

class Livro:
    def __init__(self, titulo, autor, paginas_total):
        self.titulo = titulo
        self.autor = autor
        self.paginas_total = paginas_total
        self.paginas_lida = 0
    
    def ler(self, quantidade_paginas):
        self.paginas_lida += quantidade_paginas
        if self.paginas_lida > self.paginas_total: # garantir que não ultrpasse o total de paginas
            self.paginas_lida = self.paginas_total
    
    def verificar_progresso(self):
        if self.paginas_lida == self.paginas_total:
            print(f'Parabens! Livro concluído')
        else:
            print(f'Progresso: {self.paginas_lida} de {self.paginas_total} páginas lidas.')

livro1 = Livro("Poeira em alto mar", "Desconhecido", 450)
print(livro1.paginas_total)

livro1.ler(97)
livro1.ler(99)
livro1.ler(908)

livro1.verificar_progresso()