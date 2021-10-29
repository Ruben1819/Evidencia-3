import pandas as p
import random 
sepa=("/"*10) + "\n"

#crearemos un dataframe a partir de un diccionario
diccionario_aleatorio={\
    "Ruben":[random.randrange(60,101)for x in range(4)],\
    "Saul":[80,100,57,90],"Francisco":[80,70,57,90],"Sebastian":[20,100,100,90],\
    "Paola":[100,100,100,100]}
notas= p.DataFrame(diccionario_aleatorio)
notas.index = ["Programacion","Base de datos","Contabilidad","Estructura de datos"]

notas.to_csv(r'notas.csv',index=True,header=True)
print("Exito")
pass
