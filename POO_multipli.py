#Crear una clase que permita ingresar valores enteros por teclado y nos muestre la tabla de
# multiplicar de dicho valor. Finalizar el programa al ingresar el -1.

class Multiplayer:
   
    def multiplicador(self,i=0,numero = 0):
        
        while(numero  != -1):
           numero = int(input('Ingrese un numero: '))
           i=0
          
           while (i < 13):
              print(f' {numero} X {i} = {numero*i}')
              i = i + 1 
              if(i>12):
                print("\n")

       
multi = Multiplayer()
multi.multiplicador()


# I´m done teacher :)
#Edwin Alberto Roman Seberino
#Enrollment: 2020-10233