import pandas as p

separador=("*"*20) + "\n"
notas=p.read_csv("notas.csv",index_col=0)
print(notas)
print(separador)