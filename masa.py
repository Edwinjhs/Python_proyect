from ast import If
from subprocess import IDLE_PRIORITY_CLASS


print ("Vamos a calcular cuanto pesas en otro planeta")
masa_tierra = float (input("¿Cuanto pesas en la tierra? (en kilogramos) :  "))
#peso=masa * gravedad           masa=peso/gravedad
grav_marte = 3.721
grav_nept = 11.15
grav_tierra = 9.807
resultado_peso_marte = (masa_tierra / grav_tierra) * grav_marte
resultado_peso_nept = (masa_tierra / grav_tierra) * grav_nept
#print("tu masa en marte es (kg)")
#print("{:.1f}".format(resultado_peso_marte))
#print("tu masa en neptuno es (kg)")
#print("{:.1f}".format(resultado_peso_nept))
#masa cantidad de materia en un cuerpo(aceleracion producida por su fuerza)
#peso El peso es una fuerza que actúa en todo momento, La Tierra jala a todos los objetos con una fuerza de gravedad dirigida hacia su centro.
print("Mi peso en marte es {:.2f} kg y mi peso en neptuno es {:.2f} kg".format(resultado_peso_marte, resultado_peso_nept))

if (masa_tierra > 50):
    print ("no estas gordo, solo estas en el planeta equivocado")
elif (masa_tierra < 50):
    print ("Comete alguito, estas muy flac@")
else:
    print ("Estas en tu peso ideal")