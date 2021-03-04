#Crear una funci�n que reciba una serie de edades y me retorne la cantidad que son mayores o iguales a 18.

edades18 = [] #Numero Reales de altura

def maxTo18(*args):
    
    for edad in args:
        if(edad >= 18):
            edades18.append(edad)

    print('Las edades introduccidas mayores o iguales a 18.')
    print(edades18)


maxTo18(23,4,5,7,23,12,78,39,40,18)

# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233