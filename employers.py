#Crear una aplicaci�n que se ingrese por teclado el nombre de 5 empleados, sueldo cobrado por cada 
# empleado en los ultimos 3 meses. Mostrar en pantalla el total pagado a cada empleado en los ultimos
# 3 meses obtener y mostrar cual fue el empleado de mayor ingreso.


    #ingrese por teclado el nombre de 5 empleados + sueldo
    #test = [['Emilio',70500],['Jaun',90500],['Ana',55500]]

empleados = []


for i in range(5):
    empleados.append([input('Nombre: '),int(input('3 Sueldo Acumulados:'))])
    print('\n')
def Determinar_max(empleados):
   
    extractor_sueldos = []

    for sueldo in empleados:
        extractor_sueldos.append(sueldo[1])

    for emple in empleados:
        if(emple[1] == max(extractor_sueldos)):
            print(f'{emple[0]} es el empleado con el mayor sueldo trimestral, con un sueldo de {emple[1]}')


Determinar_max(empleados)


# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233