# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

from ipaddress import summarize_address_range


print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

print('Ingrese el primer numero real:')
numero_1 = float(input())

print('Ingrese el segundo numero real:')
numero_2 = float(input())

#suma
suma = numero_1 + numero_2
print('La suma entre',numero_1,'y',numero_2,'es',suma)

#resta
resta = numero_1 - numero_2
print('La resta entre',numero_1,'y',numero_2,'es',resta)

#multiplicacion
multiplicacion = numero_1 * numero_2
print('La multiplicacion entre',numero_1,'y',numero_2,'es',multiplicacion)

#division
if numero_2 == 0: 
  print('No se puede dividir un numero por 0!!!!!!')
else:
  division = numero_1 / numero_2 
  division = round(division,2)  #con la funcion round() puedo elegir a cuantos decimales quiero redonder un numero periodico
  print('La division entre',numero_1,'y',numero_2,'es',division)
  #print('La division entre',numero_1,'y',numero_2,'es',round(division,2)) otra forma de hacerlo sin tener que redondear 
  # y despues imprimirlo en pantalla

#potencia
potencia = numero_1 ** numero_2
print('La potentencia entre',numero_1,'y',numero_2,'es',potencia)
