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
<<<<<<< HEAD
    print('###** 1.Sumar       **###')
    print('###** 2.Restar      **###')
    print('###** 3.Multiplicar **###')
    print('###** 4.Dividir     **###')
    print('###** 5.Area        **###')
    print('###** 6.Salir       **###')
=======
    print('###** 1.Sumar        **###')
    print('###** 2.Restar       **###')
    print('###** 3.Multiplicar  **###')
    print('###** 4.Dividir      **###')
    print('###** 5.Potencia     **###')
    print('###** 6.Salir        **###')
>>>>>>> rama2
    print('#########################')
   
   #vayan ampliando las operaciones de la calculadora, inventen lo que se le de la gana
    try:
          n= int(input('Elige una opción: '))
    except:
          print('Solo se aceptan numeros')
          sys.exit()


    if n==1: 
<<<<<<< HEAD
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
        
=======
        resultado = c.sumar(a,b)

    elif n==2:
        resultado = c.restar(a,b)
    
    elif n==3:
        resultado = c.multiplicar(a,b)
    
    elif n==4 and b!=0:
        resultado = c.dividir(a,b)

    elif n==5:
        resultado = c.potencia(a,b)

    elif n==6:
>>>>>>> rama2
        print("Gracias por usar la calculadora")
        x=1

    else:
        print("opción invaida")    
    
    if n>0 and n<6 and b!=0:
     print(resultado)







