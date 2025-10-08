tupla = (1,2,3,4,5) # criei uma tupla com 5 elementos (do 0 ao 4 elemento)
print(tupla) # vai mostrar: (1, 2, 3, 4, 5)
print(type(tupla)) # vai mostrar: <class 'tuple'>

# for para tupla, igual listas
for x in tupla:
    print(x) # vai mostrar em cada linha: 1, 2, 3, 4 ,5

# while para tupla, igual listas
y=0
while y < len(tupla):
    print(tupla[y]) # vai mostrar em cada linha: 1, 2, 3, 4 ,5
    y += 1