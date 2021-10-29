from typing import final
import pandas as p

inicio =int(input('Introduce el año inicial: '))
fin=int(input('Introduce el año final: '))
ventas={}
for i in range (inicio,fin+1):
    ventas[1]=float(input('Introduzca las ventas del año '+ str(1) +':'))
ventas=p.Series(ventas)
print('Ventas\n',ventas)
print('Ventas con descuentos\n', ventas*0.9)