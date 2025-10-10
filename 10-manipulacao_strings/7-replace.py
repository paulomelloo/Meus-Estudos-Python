frase = "o rato roeu a roupa do rei de roma"
print(frase)

print(frase.replace("rato", "leão")) # ira substituir a palavra rato por leao.
# vai retornar: o leão roeu a roupa do reio de roma

frase2 = "testar o replace em 2 palavras, testar. testar ira sumir"
print(frase2.replace("testar", "trocar")) # ira substituir a palavra testar por trocar. Se tiver 10x a palavra, altera as 10x.
# vai retornar: trocar o replace em 2 palavras, trocar. trocar ira sumir

print(frase2.replace("testar", "alterar", 2)) # o numero 2, limita o numero de troca que o replace faz. Nesse caso ele so vai alterar a palavra 'testar' por 'alterar' 2x.
#vai retornar: alterar o replace em 2 palavras, alterar. testar ira sumir