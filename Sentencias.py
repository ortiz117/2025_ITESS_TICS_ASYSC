#Series de Fibonacci:
# la suma de dos elementos define el siguiente
# while
a , b = 0 , 1 
while b < 1000:
 print(b, end=',')
 a, b = b, a+b

 #if
x = int(input("Ingresa un entero, por favor: "))
if x < 0:
 x = 0
 print('Negativo cambiado a cero')
elif x == 0:
 print('Cero')
elif x == 1:
 print('Simple')
else:
 print('Más')

#for
# Midiendo cadenas de texto
palabras = ['gato', 'ventana', 'defenestrado']
for p in palabras:
  print(p, len(p))

#modificar la secuencia sobre la que estás iterando
for p in palabras[:]:  # hace una copia por rebanada de toda la lista
 if len(p) > 6:
  palabras.insert(0, p)
  print(palabras)

#Range()
for i in range(5):
 print(i)

#iterar sobre los índices de una secuencia
a = ['Mary', 'tenia', 'un', 'corderito']
for i in range(len(a)):
 print(i, a[i])