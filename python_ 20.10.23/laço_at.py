#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido 
#e continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite uma nota (0 - 10):"))

while nota < 0 or nota > 10:
    print("Este valor é inválido")
    nota = float(input("Digite novamente (0 - 10):"))

print("Número válido")

#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.

for i in range(1,21,1):
    print(i) 

#Faça um programa que imprima na tela os números pares de 1 a 100.

for i in range(2,101,2):
    print(i) 

#Faça um programa que imprima na tela os números impares de 1 a 100.

for i in range(1,101,2):
    print(i) 

#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada.

numero=int(input("Escolha qual tabuada você quer (1-10)"))

for i in range(11):
    print(numero, "x", i, "=", numero*i)

#Faça um programa que, dado um conjunto de N números,
#determine o menor valor, o maior valor e a soma dos valores.

#tentei fazer usando a lista mas não deu certo

#Lista = []
#Lista.append("coloque o primeiro valor")
#Lista.append("coloque o segundo valor")
#Lista.append("coloque o terceiro valor")
#Lista.append("coloque o quarto valor")

#Lista.sort()
#print(Lista)
#Lista.index(1)
#Lista.index(2)

N = int(input("escolha uma quantidade de numeros: "))
menor = float("inf")
maior = float("-inf")
soma = 0


for i in range(N):
    numero = float(input(f"escreva um numero: {1+1}"))
    
    if numero < menor:
        menor = numero
        
    if numero > maior:
        maior = numero
        
    soma += numero
    
print("menor: ", menor) 
print("maior: ", maior)    
print("soma: ", soma)