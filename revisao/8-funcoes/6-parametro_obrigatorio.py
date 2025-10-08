def soma(a,b,c=8,d=10): #sempre colocar o parametro opicional por ultimo (no caso o C e D). NUNCA COLOCAR O OBRIGATORIO POR ULTIMO
    print(a + b + c + d)

soma(1,2) # não precisei passar o parametro C e D pois ja tem a opção na função
#vai retornar 21 (1+2+8+10)
soma(1,2,3,4) # se eu quiser substituir o parametro opcional C e D é só eu SETAR quando for chamar a função
#vai retornar 10 (1+2+3+4)