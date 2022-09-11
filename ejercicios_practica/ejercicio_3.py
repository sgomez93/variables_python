# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo
print('Nombre completo:',nombre,apellido)

# Almacenar su nombre completo en una variable
# nombre_completo = .....

nombre_completo = nombre + apellido

# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
cantidad_letras = len(nombre_completo)
print('Su nombre tiene',cantidad_letras,'letras')

#Me faltaria identificar si ingresa mas de un nombre y apellido porque sino en cantidad de letras cuenta de mas porque 
#suma los espacios