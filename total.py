import  datetime
from subprocess import call

#datos del usuario
archivo1 = open("datos_usuario.txt","r")
datos = archivo1.readlines()
lista1 = []
for j in datos:
    fix = j.strip().split(":")
    lista1.append(fix)
print("\nDatos personales del usuario en forma lista: ",lista1)
#convertiendo a diccionario
diccionario = dict(lista1)
print("\nDatos personales del usuario en forma diccionario: ",diccionario)

#lista de compras
archivo2 = open("compras.txt","r")
boleta = archivo2.readlines()
lista2 = []
for i in boleta:
    arreglo = i.strip().split(":")
    lista2.append(arreglo)
print("\nLista de su boleta de compras de productos con su precio: ",lista2)

#hora del registro
tiempo = datetime.datetime.now()
#boleta
boleta = open("boleta.txt","w",encoding="utf8")
#titulo
boleta.write(("Boleta de Tu Opcion Saludable").center(60,"="))
#hora del registro
boleta.write(tiempo.strftime("\nFecha: %y-%m-%d \nHora: %H:%M\n"))
#datos en tipo diccionario
boleta.write("\nDatos del usuario: "+str(diccionario)+"\n")
#tabla de lista de canciones con format
boleta.write("\n"+"-"*50+"\n")
cont = 0
suma = 0
boleta.write("{2:>7}{0:^25}{2}{1:^15}{2}\n".format("PRODUCTO","IMPORTE","|"))
boleta.write("-"*50+"\n")
for j in lista2:
    cont += 1
    suma += float(j[1])
    boleta.write("{3}{0:^5}{3:<2}{1:<25}{3:<2}{2:>10,.2f}{3:>4}\n".format(cont,j[0],float(j[1]),"|"))
    boleta.write("-"*50+"\n")
boleta.write("{0:>19}{2:>15}{1:>10,.2f}\n".format("TOTAL",suma,"|"))
boleta.write("-"*50+"\n")

boleta.close()