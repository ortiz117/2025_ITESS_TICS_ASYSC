# Definir una función para escribir la serie de Fibonacci
def fib(n):
    """Escribe la serie de Fibonacci hasta n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Llamar a la función que acabamos de definir
fib(2000)

# Asignar una función a otra variable
f = fib
f(100)

# Ver el valor de retorno de una función que no retorna nada explícitamente (retorna None)
fib(0)
print(fib(0))

# Escribir una función que retorne una lista con la serie de Fibonacci
def fib2(n):
    """Devuelve una lista conteniendo la serie de Fibonacci hasta n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# Llamar a la nueva función y ver su resultado
f100 = fib2(100)
f100

# Definir una función con argumentos con valores por omisión
def pedir_confirmacion(prompt, reintentos=4, queja='Si o no, por favor!'):
    while True:
        ok = input(prompt)
        if ok in ('s', 'S', 'si', 'Si', 'SI'):
            return True
        if ok in ('n', 'no', 'No', 'NO'):
            return False
        reintentos = reintentos - 1
        if reintentos < 0:
            raise OSError('usuario duro')
        print(queja)

# Ejemplo de cómo se evalúa el valor por omisión solo una vez
i = 5
def f(arg=i):
    print(arg)
i = 6
f()

# Función que acumula argumentos en llamadas subsiguientes (comportamiento inesperado)
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

# Forma correcta de evitar que el valor por omisión sea compartido
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# Función con argumentos de palabra clave (nombrados)
def loro(tension, estado='muerto', accion='explotar', tipo='Azul Nordico'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.")
    print("-- Gran plumaje tiene el", tipo)
    print("-- Está", estado, "!")

# Diferentes formas de llamar a la función 'loro'
loro(1000)
loro(tension=1000)
loro(tension=1000000, accion='VOOOOOM')
loro(accion='VOOOOOM', tension=1000000)
loro('un millón', 'despojado de vida', 'saltar')
loro('mil', estado='viendo crecer las flores desde abajo')

# Ejemplo de llamada que falla por recibir un valor duplicado para un argumento
#def funcion(a):
#    pass
# funcion(0, a=0) # Esto generaría un TypeError

# Función que acepta argumentos posicionales y nombrados arbitrarios
def ventadequeso(tipo, *argumentos, **palabrasclaves):
    print("-- ¿Tiene", tipo, "?")
    print("-- Lo siento, nos quedamos sin", tipo)
    for arg in argumentos:
        print(arg)
    print("-" * 40)
    claves = sorted(palabrasclaves.keys())
    for c in claves:
        print(c, ":", palabrasclaves[c])

# Llamada a la función 'ventadequeso'
ventadequeso("Limburger", "Es muy liquido, sr.",
             "Realmente es muy muy liquido, sr.",
             cliente="Juan Garau",
             vendedor="Miguel Paez",
             puesto="Venta de Queso Argentino")

# Función con argumentos "sólo nombrados" después de *args
def concatenar(*args, sep="/"):
    return sep.join(args)

concatenar("tierra", "marte", "venus")
concatenar("tierra", "marte", "venus", sep=".")

# Desempaquetar una lista de argumentos para llamar a una función
list(range(3, 6))
args = [3, 6]
list(range(*args))

# Desempaquetar un diccionario para entregar argumentos nombrados
def loro(tension, estado='rostizado', accion='explotar'):
    print("-- Este loro no va a", accion, end=' ')
    print("si le aplicás", tension, "voltios.", end=' ')
    print("Está", estado, "!")

d = {"tension": "cinco mil", "estado": "demacrado", "accion": "VOLAR"}
loro(**d)

# Crear pequeñas funciones anónimas (lambda)
def hacer_incrementador(n):
    return lambda x: x + n

f = hacer_incrementador(42)
f(0)
f(1)

# Ejemplo de una cadena de documentación (docstring) de varias líneas
def mi_funcion():
    """No hace mas que documentar la funcion.
    No, de verdad. No hace nada.
    """
    pass

print(mi_funcion.__doc__)

# Ejemplo de anotaciones de funciones
def f(jamon: str, huevos: str = 'huevos') -> str:
    print("Anotaciones:", f.__annotations__)
    print("Argumentos:", jamon, huevos)
    return jamon + ' y ' + huevos

f('carne')