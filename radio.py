#¿Cómo sacar el área y la circunferencia de un círculo dado el radio en Python?
#construye un programa que al  recibir como dato el radio de un circulo, calcule e imprima tanto su area como su longitud de circunferencia
#el area de un circulo es are= pi * radio'2
#la circunferencia de un circulo es longitud =2 *pi * radio

from cmath import pi


radio = float(input("Por favor introduzca el radio del circulo= "))
area= pi * (radio)**2
circunferencia = 2 * pi * radio

print ("El area de ese circulo es= {:.2f}".format (area))
print ("La longitud de ese circulo es= {:.2f}".format (circunferencia))
print (pi)
