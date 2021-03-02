"""
Un programa que pida al usuario 4 n�meros, los memorice (utilizando una coleccion), calcule su media aritm�tica
y despu�s muestre en pantalla la media y los datos ingresado.
"""

numbers = []
promedio = 0


for i in range(4):
    numbers.append(int(input('Ingrese un numero: ')))

for nums in numbers:
   promedio+= nums

print(f'Su media aritm�tica es {promedio//len(numbers)}')