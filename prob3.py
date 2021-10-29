#Escribri una funcion que reciba un diccionario con las notas de los alumnos en curso en un examen
#y devuelva una serie con las notas de los alumnos aprobados ordenados de mayor a menor
import pandas as p

def aprobados(notas):
    notas=p.Series(notas)
    return notas[notas >=5].sort_values(ascending=False)
notas={'Raul':9,'Fer':6.6,'Juan':3,'Rosa':9.5,'Luis':5}
print(aprobados(notas))