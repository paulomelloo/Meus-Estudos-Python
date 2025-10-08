for x in range(0,7):
    print(x) # ira 'criar'/mostrar os elementos 0,1,2,3,4,5,6 (linha por linha)

print("---") #separador para nao mostrar um range em seguida do outro

for y in range(5,11):
    print(y) # ira 'criar'/mostrar os elementos 5,6,7,8,9,10 (linha por linha), começou do elemento 5 e foi até o 10

print("---")

for z in range(0,11,2): # 0 elemento inicial, 11 elemento final, 2 ira pegar os numeros de 2 em 2
    print(z) # então ira mostrar 0,2,4,6,8,10 (pegou de 2 em 2 os elementos 0 a elemento 11), se quiser os impares so troca o range para range(1,10,2)