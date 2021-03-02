#Crear una lista. La lista tiene que tener 3 elementos. Cada elemento debe ser una lista de 5 enteros. 
# Calcular y mostrar la suma de cada lista contenida en la lista principal.


mainList = [[1,2,3,4,0],[12,-12,31,31,34],[1355,64,63,32,6]]

for key,i in enumerate(mainList):
    temp = 0
    for x in i:
        temp+=x

    print(f'Suma de la Sub_lista_{key+1}: {temp}')