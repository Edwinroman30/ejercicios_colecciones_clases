#Crear una lista y almacenar 20 enteros pedidos por teclado. Eliminar todos los elementos que sean pares.

num_enteros = []

try:
    for i in range(20):
        num_enteros.append(int(input('Digite un numero entero: ')))
except:
    print('Ha ocurrido un error al ingresar los numero....')


def filter_odds(lista_num):

    for num in lista_num:
        if(num%2 == 0):
            num_enteros.remove(num)


filter_odds(num_enteros)
print('Resultado final....')
print(num_enteros)

