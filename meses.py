#Un programa que almacene en una lista el n�mero de d�as que tiene cada mes
#(supondremos que es un a�o no bisiesto), pida al usuario que le indique un mes 
#(1=enero, 12=diciembre) y muestre en pantalla el n�mero de d�as que tiene ese mes.


print('1)enero 2)febrero 3)marzo 4)abril  5)mayo 6)junio9')
print('7)julio 8)agosto  9)septiembre 10)octubre 11)noviembre 12)diciembre \n')

Dmese = {
    1: ['enero',30],
    2: ['febrero',28],
    3: ['marzo',31],
    4: ['abril',30],
    5: ['mayo',31],
    6: ['junio',30],
    7: ['julio',31],
    8: ['agosto',31],
    9: ['septiembre',30],
    10: ['octubre',31],
    11: ['noviembre',30],
    12: ['diciembre',31]
}

opcion = int(input('Inserte el valor:'))

print(f'{Dmese[opcion][0]} tiene {Dmese[opcion][1]}  días.')