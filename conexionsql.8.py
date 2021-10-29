import sqlite3
from sqlite3 import Error

try:
    with sqlite3.connect("PrimerIntento.db") as conn:
        print(sqlite3.version)
except Error as e:
    print(e)

#El bloque with es un manejador de contexto