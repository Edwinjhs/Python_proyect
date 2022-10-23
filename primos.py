
def num_p():
    num = int (input("Introduce el numero a comprobar: "))
    list=[i for i in range(2,num) if num % i == 0 ]
    if num ==2:
        print ("Es un numero primo")
    elif len(list)!=0:
        print("El numero", num ," No es un numero primo")
    elif num == 1:
        print ("no es primo")
    else:
        print("El numero", num ," Si es un numero primo")  
num_p()



"""
print ("POR FAVOR INGRESE EL NUMERO n1 QUE QUIERE EVALUAR SI ES O NO PRIMO")
num = int (input("Por favor introduce el numero:  "))
if num <=1:
    print ("El numero ",num ," no es un numero primo")
elif num == 2:
    print ("El numero ", num ," es un numero primo")
def ciclo ():
    modulo = num % 2
    if modulo == 0:
        print ("no es un numero primo")
    elif modulo != 0:
        for i in range (2,num):
            modu = num % i
            if modu == 0:
                print ("No es primo")        
            else:
                print ("es primo")
#            if num % i !=0:
#               print ("el numero ", num,(" es primo"))
ciclo ()

print ("POR FAVOR INGRESE EL NUMERO n1 QUE QUIERE EVALUAR SI ES O NO PRIMO")
num = int (input("Por favor introduce el numero:  "))
if num <=1:
    print ("El numero ",num ," no es un numero primo")
elif num == 2:
    print ("El numero ", num ," es un numero primo")
for i in range (2,num):
    if (num % i) != 0:
        print ("Es primo")
        break
    elif (num % i) != 0:
        print ("No es primo")
        break

num = int (input ("Introduce un numero para probar si es o no primo:  "))
for i in range (2,num):
    modulo = num % i
    if modulo == 0:
        break
 """