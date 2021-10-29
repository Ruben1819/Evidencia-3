#Escribir una funcion que reciba un diccionario con las notas de los alumnos
#en curso en un examen y devuelva una serie con la nota minima,la maxinma,media 
#y la desviacion tipica
import pandas as p

def estadistica(notas):
    notas =p.Series(notas)
    estadis=p.Series([notas.min(),notas.max(),notas.mean(),notas.std(),], index=['MIN','MAX','MEDIA','DESVIACION'])
    return estadistica

notas= {'Juan':9,'Francisco':6,'Ruben':7.8,'Luis':8.2,'Raul':5}
print(estadistica(notas))