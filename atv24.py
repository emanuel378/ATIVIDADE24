# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.
soma = 0
contador = 0

while True:
    n=int(input("Digite um número e quando quiser para,-1 para parar: "))
    
    if n ==-1:
        break
    soma+=n
    contador+=1

    if contador>0:
        media = soma/contador
print(media)
        
   

