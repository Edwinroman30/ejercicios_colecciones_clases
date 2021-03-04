#Crear y cargar una lista con 10 enteros por teclado. Crear un programa que identifique el valor mas
# peque�o de la lista y la posici�n donde se encuentra. Mostrar en pantalla el resultado.


lista = []
selection = []

for i in range(10):
    lista.append(int(input('Ingrese un numero: ')))

def identifier(data):
        
    selection.append(lista.index(min(lista)))
    selection.append(min(lista))

    print(f'El numero mas pequeño es {selection[1]} y esta en el indice {selection[0]}, de la siguiente lista:')
   


identifier(lista)


# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233