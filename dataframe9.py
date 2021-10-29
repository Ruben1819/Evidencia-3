import pandas as p
import random
separador=("/"*20) + '\n'

diccionario_not={"Ruben":[87,100,None],"Raul":[80,None,57],\
                 "Lindolfo":[80,70,57],"Panfilo":[20,100,100],\
                 "Fernanda":[100,100,100]}

notas_dic=p.DataFrame(diccionario_not)
print(notas_dic)
print(separador)

diccionario_notaleat={\
    "Ruben":[random.randrange(60,101)for x in range(3)],\
    "Raul":[80,100,57],"Lindolfo":[80,70,57],"Panfilo":[20,100,100],\
    "Fernanda":[100,100,100]}

notas_dic=p.DataFrame(diccionario_notaleat)
print(notas_dic)
print(separador)

notas_dic.index=["Programacion","Base de Datos","Contabilidad"]
print(notas_dic)
print(separador)