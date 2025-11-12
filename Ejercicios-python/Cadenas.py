HuevosPan = 'huevos y pan' # comillas simples
doesnt = 'doesn\'t' 
"\n" "doesn't"  # usa \' para escapar comillas simples...
"doesn't"  # ...o de lo contrario usa comillas doblas
siledijo = '"Si," le dijo.' 
"\n" '"Si," le dijo.' 
"\n" "\"Si,\" le dijo."
print(HuevosPan)
print(doesnt)
print(siledijo)

print('C:\algun\nombre')  # aquí \n significa nueva línea!
print(r'C:\algun\nombre')  # nota la r antes de la comilla

#múltiples líneas
print("""\
 Uso: algo [OPTIONS]
     -h                        Muestra el mensaje de uso
     -H nombrehost             Nombre del host al cual conectarse
 """)

# 3 veces 'un', seguido de 'ium'
print(3 * 'un' + 'ium')

#Concatenar
print('Py' 'thon')

#concatenar variables o una variable con un literal
prefix = "py"
print(prefix + 'thon')

#separar cadenadas largas
texto = ('Poné muchas cadenas dentro de paréntesis '
             'para que ellas sean unidas juntas.')
print(texto)

#(subíndices)
palabra = 'Python'
print(palabra[0])  # caracter en la posición 0
print(palabra[5])  # caracter en la posición 5

# números negativos, para empezar a contar desde la dereche
print(palabra[-1])  # caracter en la posición -1
print(palabra[-2])  # caracter en la posición -2
print(palabra[-6])  # caracter en la posición -6

#rebanadas te permiten obtener sub-cadenas
print(palabra[0:2])  # caracteres desde la posición 0 (incluída) hasta la 2 (excluída)
print(palabra[2:6])  # caracteres desde la posición 2 (incluída) hasta la 5 (excluída)

#Esto asegura que s[:i] + s[i:] siempre sea igual a s:
print(palabra[:2] + palabra[2:])
print(palabra[:4] + palabra[4:])

#cadenas de Python no pueden ser modificadas -- son immutable
#palabra[0] = 'J'
#print(palabra)

#Si necesitás una cadena diferente, deberías crear una nueva
print('J' + palabra[1:])
print(palabra[:2] + 'py')

#len() devuelve la longitud de una cadena de texto
s = 'supercalifrastilisticoespialidoso'
print(len(s))