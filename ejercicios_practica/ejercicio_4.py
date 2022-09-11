# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
from itertools import accumulate


print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

print('Ingrese palabra 3:')
palabra_3 = str(input())

# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla

#1ra Forma
# = palabra_1[0] + palabra_2[0] + palabra_3[0]  #concateno el primer caracter de cada palabra
#print('El acronimo de',palabra_1,',',palabra_2,',',palabra_3,'es:',acronimo.upper()) #directamente en el print paso a mayuscula

#2da forma
#acronimo = palabra_1[0] + palabra_2[0] + palabra_3[0]
#acronimo_M = acronimo.upper()  #Transformo las palabras a mayuscula con la funcion upper()
#print('El acronimo de',palabra_1,',',palabra_2,',',palabra_3,'es:',acronimo_M)

#3ra forma
#Transformo el primer caracter de cada palabra con la funcion capitalize() y luego lo concateno
acronimo = palabra_1.capitalize()[0] + palabra_2.capitalize()[0] + palabra_3.capitalize()[0]
print('El acronimo de',palabra_1,',',palabra_2,',',palabra_3,'es:',acronimo)

