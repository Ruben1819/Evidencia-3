#El modulo csv implemeta clases para leer y escribir datos tabulares en formato csv
#Permite a los programadores decir,escribe datos en el formato preferido por excel
#o lee datos de este archivo que fue generado por excel,sin conoces los detalles especificos
#del formato csv usado por excel
import csv
columnas =("clave","nombre","correo")
datos=[[1,"RAUL","raul@gmail.com"],
      [2,"RUBEN","ruben@hotmail.com"],
      [3,"Samy",None]]

with open ("datos.csv","w",newline="") as archivo:
    registro=csv.writer(archivo)
    registro.writerow(columnas)
    #tambien puede ser
    #for registro in datos:
       #registrador.writerow(registro)
    registro.writerows(datos)

columnas=None
datos=list()

with open("datos.csv","r") as archivo:
    lector=csv.reader(archivo,delimiter=",")
    registro=0
    for clave,nombre,correo in lector:
        if registro==0:
            columnas=(clave,nombre,correo)
            registro=registro+1
        else:
            clave=int(clave)
            datos.append([clave,nombre,correo])
print(datos)

