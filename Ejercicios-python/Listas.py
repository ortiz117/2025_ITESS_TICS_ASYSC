#Listas
cuadrados = [1, 4, 9, 16, 25]
print(cuadrados)

# pueden ser indexadas y rebanadas
print(cuadrados[0])  # índices retornan un ítem
print(cuadrados[-1])
print(cuadrados[-3:])

#concatenacion
print(cuadrados + [36, 49, 64, 81, 100])

# listas son un tipo mutable
cubos = [1, 8, 27, 65, 125]  # hay algo mal aquí
print(cubos)
cubos[3] = 64  # reemplazar el valor incorrecto
print(cubos)

#método append()
cubos.append(216)  # agregar el cubo de 6
print(cubos)
cubos.append(7 ** 3)
print(cubos)

#asignar a una rebanada
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letras)
# reemplazar algunos valores
letras[2:5] = ['C', 'D', 'E']
print(letras)
# ahora borrarlas
letras[2:5] = []
print(letras)
# borrar la lista reemplzando todos los elementos por una lista vacía
#letras[:] = []
#print(letras)

#len() también sirve para las listas
print(len(letras))

#anidar listas (crear listas que contengan otras listas)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])