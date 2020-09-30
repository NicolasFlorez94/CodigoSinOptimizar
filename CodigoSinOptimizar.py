import math

lst = [] 
  
n = int(input()) 
  
for i in range(0, n): 
    ele = input()
    price = int(input())
    lst.append(ele)
    lst.append(price)


contador = 0
if len(lst) > contador:
    productoUno = lst[0]
    precioUno = lst[1]
    contador = 2
    conteoProducto = 1
if len(lst) > contador:
    productoDos = lst[2]
    precioDos = lst[3]
    contador = 4
    conteoProducto = 2
if len(lst) > contador:
    productoTres = lst[4]
    precioTres = lst[5]
    contador = 6
    conteoProducto = 3
if len(lst) > contador:
    productoCuatro = lst[6]
    precioCuatro = lst[7]
    contador = 8
    conteoProducto = 4
if len(lst) > contador:
    productoCinco = lst[8]
    precioCinco = lst[9]
    contador = 10
    conteoProducto = 5

sumaTotal = precioUno
if conteoProducto == 2:
    sumaTotal = precioUno + precioDos
if conteoProducto == 3:
    sumaTotal = precioUno + precioDos + precioTres
if conteoProducto == 4:
    sumaTotal = precioUno + precioDos + precioTres + precioCuatro
if conteoProducto == 5:
    sumaTotal = precioUno + precioDos + precioTres + precioCuatro + precioCinco

descuento = 0
precioConDescuento = sumaTotal
if sumaTotal > 150000:
    descuento = (sumaTotal * 10 ) / 100
if sumaTotal > 300000:
    descuento = (sumaTotal * 15 ) / 100
if sumaTotal > 700000:
    descuento = (sumaTotal * 20 ) / 100
precioConDescuento = sumaTotal - descuento

print ("Centro Comercial Unaleño")
print ("Compra más y Gasta Menos")
print ("NIT 899.999.063")
if conteoProducto == 1:
    print (productoUno + " $" + str(precioUno))
if conteoProducto == 2:
    print (productoUno + " $" + str(precioUno))
    print (productoDos + " $" + str(precioDos))
if conteoProducto == 3:
    print (productoUno + " $" + str(precioUno))
    print (productoDos + " $" + str(precioDos))
    print (productoTres + " $" + str(precioTres))
if conteoProducto == 4:
    print (productoUno + " $" + str(precioUno))
    print (productoDos + " $" + str(precioDos))
    print (productoTres + " $" + str(precioTres))
    print (productoCuatro + " $" + str(precioCuatro))
if conteoProducto == 5:
    print (productoUno + " $" + str(precioUno))
    print (productoDos + " $" + str(precioDos))
    print (productoTres + " $" + str(precioTres))
    print (productoCuatro + " $" + str(precioCuatro))
    print (productoCinco + " $" + str(precioCinco))
print ("Total: $" + str(math.ceil (precioConDescuento)))
print ("En esta compra tu descuento fue $" + str( math.floor (descuento)))
print ("Gracias por tu compra")
