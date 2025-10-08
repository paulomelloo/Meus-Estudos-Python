import funcoes # importa as funcoes do arquivo funcoes.py
import cart #importa as funcoes do arquivo cart.py

funcoes.ola_modulo() # importa e executa a função ola_modulo (do arquivo funcoes.py) resultado: Ola mundo!
funcoes.ola_nome('Paulo') # importa e executa a função ola_nome (do arquivo funcoes.py) resultado: Ola Paulo
funcoes.soma(4, 2) # importa a funcao soma, resultado: 2

produto = ["camiseta", 75] # cria a lista com 2 elementos para usar na funcao carrinho_compra (do arquivo cart.py)
cart.carrinho_compra(produto) # importa e executa a funcao carrinho_compra. Vai mostrar: O produto é camiseta e seu preço é R$75