import sys
from Calculator import Calc
from Operaciones import Operator
  #Creamos el objeto de la clase calculadora
     
c=Operator()
x=0
while x!=1: 
    
    try: 
        a= float(input('Indica el Valor del Primer Numero: '))
        b=float (input('Indica el valor del Segundo Numero: '))
    except:
        print('Solo se aceptan numeros')
        sys.exit()
       

    print('Selecciona la operacion que quieras realizar: ')
    print('#########################')
    print('###** 1.Sumar       **###')
    print('###** 2.Restar      **###')
    print('###** 3.Multiplicar **###')
    print('###** 4.Dividir     **###')
    print('###** 5.Area        **###')
    print('###** 6.Salir       **###')
    print('#########################')
   
   #vayan ampliando las operaciones de la calculadora, inventen lo que se le de la gana
    try:
          n= int(input('Elige una opción: '))
    except:
          print('Solo se aceptan numeros')
          sys.exit()


    if n==1: 
        resultado=c.sumar(a,b)

    if n==2:
        resultado=c.restar(a,b)
    if n==3:
        resultado=c.multiplicar(a,b)
    if n==4 and b!=0:
        resultado=c.dividir(a,b)
    if n==5:
        resultado=c.Area(a,b)

    if n==6 or b==0:
        if b==0:
           print("Division por cero no es posible") 
        
        print("Gracias por usar la calculadora")
        x=1
        
    
    if n>0 and n<6 and b!=0:
     print(resultado)







