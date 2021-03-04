#Crear un programa que defina una lista de 5 elementos de tipo reales que representen las alturas de 5 personas.
#Obtener el promedio de las mismas. Contar cu�ntas personas son m�s altas que el promedio y cu�ntas m�s bajas.


real_nums = [] #Numero Reales de altura
suma_altura = 0
promedio = 0

max_prom =[]
min_prom =[]

for i in range(5):
     real_nums.append(float(input('INGRESA SU ALTURA: ')))

for valores in real_nums:
    suma_altura = suma_altura + valores

promedio = suma_altura / len(real_nums)

def Determinador():

    for estaturas in real_nums:
        if(estaturas > promedio):
            max_prom.append(estaturas)
        else:
            min_prom.append(estaturas)
    
    print(f'Las estaturas mayores al promedio: {max_prom}')
    print(f'Las estaturas menores al promedio: {min_prom}')

print("\n")
print(f'Su promedio es... {round(promedio)}')
Determinador()


# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233