import pandas as p
import random
separador=("/"*15) + '\n'

#creacion de un dataframe a partir de un dicionario
diccionario_aleatorio={\
    "Ruben":[random.randrange(60,101)for x in range(3)],\
    "Fernanda":[80,100,57],"Juan":[80,70,57],"Panfilo":[20,100,100],\
    "Raul":[100,100,100]}
notas=p.DataFrame(diccionario_aleatorio)
notas.index=["Programacion","Base de datos","Contabilidad"]

#Accesas renglones utilizando slices
#IMPORTANTE:El final del slice si esta incluido
print("Todas las asignaturas,todos los estudiantes")
subconjunto=notas.loc["Programacion":"Contabilidad"]
print(subconjunto)
x=input("Presiona una tecla : ")
print(separador)

print("Ultimas dos asignaturas,todos los estudiantes")
subconjunto=notas.loc["Base de datos":"Contabilidad"]
print(subconjunto)
print(separador)

print("Subconjunto,solamente las notas de Juan y Raul para las primeras dos asignaturas")
subconjunto=notas.loc["Programacion":"Base de datos",["Juan","Raul"]]
print(subconjunto)
print(separador)

#index booleano
print("Solamente calificaciones aprobatorias")
aprobados=notas[notas >=70]
print(aprobados)
print(separador)

print("Solamente calificacion aprobatorias entre 70 y 80")
aprobados=notas[(notas >= 70)& (notas<= 80)]
print(aprobados)
print(separador)

print("Solamente calificaciones no aprobatorias que sean pares")
reprobados=notas[(notas <=70)&(notas %2==0)]
print(reprobados)
print(separador)

#Accesar a datos especificos
print("La calificacion de 'Panfilo' en 'Programacion' ")
nota_panfilo=notas.at["Programacion","Panfilo"]
print(nota_panfilo)
print(separador)

#Modificar valores directamente
print("Modificar la nota de Panfilo en programacion")
notas.at["Programacion","Panfilo"]=80
nota_panprograma=notas.at["Programacion","Panfilo"]
print(nota_panprograma)
