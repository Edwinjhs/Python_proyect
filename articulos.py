#construye un programa que, al recibir como datos el costo de un articulo vendido y la cantidad  de dinero entregado por el cliente, calcular:
#1. el cambio que se debe entregar al cliente, si el pago efectuado es mayor que el precio del producto.
#2. ¿que pasa si el cliente paga exactamente lo que vale el producto?
#3. la cantidad de dinero que falta por pagar, si el pago efectuado es menor que el precio del producto
precio = float (input("INGRESE EL PRECIO DEL ARTICULO  "))
pago = float (input("¿CUANTO PAGO EL CLIENTE? "))
cambio = pago - precio
faltante = precio - pago
if (cambio<0):
    print ("Falta dinero en el pago. El dinero faltante es ", faltante)
elif (cambio == 0):
    print ("Se ha pagado el dinero exacto, No es necesario dar cambio ")
if (cambio > 0):
    print ("El cambio a dar es ", cambio)

