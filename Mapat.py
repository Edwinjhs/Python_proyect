from cgitb import text
from webbrowser import Elinks
g_o = "GAME OVER"

print ("Bienvenido al Mapa del tesoro")
print ("a continuacion se te presentaran una serie de decisiones las cuales te llevaran al tesoro")
caminoID = input ("Hay dos caminos, cual escoges derecha o izquierda(debes escribir derecha o izquierda):  ")
if caminoID != "derecha" or caminoID != "izquierda":
#   while caminoID != "izquierda" or caminoID != "derecha":
#       print ("el dato ingresado es incorrecto, vuelve a intentar")
#       caminoID = input ("Hay dos caminos, cual escoges derecha o izquierda(debes escribir derecha o izquierda):  ")
#       if caminoID == "derecha" or caminoID== "izquierda":
#
# break
    if caminoID == "derecha":
        print ("caiste en un agujero")
        print ("caiste sobre un nido de avestruces y hay 3 huevos, debes escoger uno de ellos  ")
        huevo = input ("¿cual abres?(amarillo, azul, blanco)")
        if huevo == "amarillo":
            print ("Felicitaciones, obtuviste mucha energia para seguir tu camino  ")
            print ("Se abrio un portal que te llevo directo al tesoro perdido, pero deberas elegir pasar entre tiburones o anguilas electricas")
            tib_ang = input ("¿Tiburones o anguilas?  ")
            if tib_ang == "tiburones":
                print ("Felicitaciones obtuviste el cofre, eran tiburones gatos que son inofensivos")
                print ("WIN")
            elif tib_ang == "anguilas":
                print ("Mala suerte, las anguilas te electrocutaron.")
                print (g_o)
            else:
                print ("lo siento, debes introducir tiburones o anguilas")
        elif huevo == "blanco":
            print ("Mala suerte, habia un bebe avestruz y te comio")
            print (g_o)
        elif huevo == "azul":
            print ("Felicidades, obtuviste mucha energia para seguir tu camino")
            print ("Ahora se abrio un portal y encontraste una piscina")
        nad_esp = input ("nado o espero")
        if nad_esp=="espero":
            print("Llega un huracan y mueres, "+ g_o)
        elif nad_esp=="nado":
            print("Encontrates 3 puertas, cual eliges?:")
            cual_puert = input ("¿Cual puerta escoges?(azul, roja, verde)")
            if cual_puert == "roja":
                print ("llegaste a la cueva de fuego te quemaste"+g_o)
            elif cual_puert == "azul":
                print ("llegaste a una cueva repleta de cocodrilos, te comieron."+ g_o)
            elif cual_puert == "verde":
                print ("llegaste directo al tesoro perdido, se encuentra encima de una palmera")
                esca_cae = input ("¿Lo escalas o lo mueves hasta que caiga? (escalar o mover")
                if esca_cae == "mover":
                    print ("Se te cayo encima y te aplasto" + g_o)
                elif esca_cae == "escalar":
                    print ("Obtuviste el cofre, ¡Felicidades!")
                    print ("WIN, obtuviste el cofre, felicidades")
                else:
                    print ("debes escoger entre escalar o mover, la respuesta dada no es valida")
            else:
                print ("debes escoger entre la puerta azul, roja o verde. la opcion dada no es valida")
        else:
            print("la opcion no esta disponible")     
    else:
        print("La opcion que elejistes no esta disponible")   
elif caminoID == "izquierda":
    print ("Encontraste una piscina")
    nad_esp = input ("nado o espero")
    if nad_esp=="espero":
        print("Llega un huracan y mueres, "+ g_o)
    elif nad_esp=="nado":
        print("Encontrates 3 puertas, cual eliges?:")
        cual_puert = input ("¿Cual puerta escoges?(azul, rojo, verde)")
        if cual_puert == "rojo":
            print ("llegaste a la cueva de fuego te quemaste"+g_o)
        elif cual_puert == "azul":
            print ("llegaste a una cueva repleta de cocodrilos, te comieron."+ g_o)
        elif cual_puert == "verde":
            print ("llegaste directo al tesoro perdido, se encuentra encima de una palmera")
            esca_cae = input ("¿Lo escalas o lo mueves hasta que caiga? (escalar o mover")
            if esca_cae == "mover":
                print ("Se te cayo encima y te aplasto" + g_o)
            elif esca_cae == "escalar":
                print ("Obtuviste el cofre, ¡Felicidades!")
                print ("WIN, obtuviste el cofre, felicidades")
            else:
                print ("debes escoger entre escalar o mover, la respuesta dada no es valida")
        else:
                print ("debes escoger entre la puerta azul, roja o verde. la opcion dada no es valida")


else:
    print ("debes escoger uno de los dos caminos indicados, el que escogiste no existe")

