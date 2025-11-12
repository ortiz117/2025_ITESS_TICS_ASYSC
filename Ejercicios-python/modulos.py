#Importar un módulo y usar sus funciones
import fibo
fibo.fib(1000)
fibo.fib2(100)
fibo.__name__

# Asignar una función de un módulo a un nombre local
fib = fibo.fib
fib(500)

# Importar nombres específicos de un módulo
from fibo import fib, fib2
fib(500)

# Importar todos los nombres de un módulo (no recomendado en general)
from fibo import *
fib(500)

# # --- Agregar esto al final de fibo.py para hacerlo ejecutable ---
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))