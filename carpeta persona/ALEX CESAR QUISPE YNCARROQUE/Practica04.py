# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:02:52 2024

@author: HP
"""
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 2024

@author: HP
"""

#%% Desarrollo de Estructuras Iterativas
"""
Uso del bucle 'for'

1. Estructura Iterativa - Bucle 'for'

El bucle 'for' se utiliza para recorrer los elementos de un objeto iterable 
(lista, tupla, string, diccionario, etc.) y ejecutar un bloque de código.
En cada paso de la iteración, se tiene en cuenta un único elemento del objeto 
iterable, sobre el cual se pueden aplicar una serie de operaciones.

Sintaxis básica del bucle 'for':
    for <variable> in <iterable>:
        <código>
"""

#%% Iterar sobre una lista
# Iterar sobre una lista de colores
# El siguiente programa recorre una lista de colores y crea una nueva lista 
# con todos los colores que contienen la letra 'r'.

# Lista original de colores
colores = ["rojo", "azul", "verde", "amarillo", "morado", "rosa"]

# Nueva lista que almacenará los colores con la letra "r"
colores_con_r = []

# Bucle for para recorrer los colores
for color in colores:
    if "r" in color:    # Verificar si el color contiene la letra "r"
        colores_con_r.append(color)    # Añadir el color a la nueva lista

# Mostrar la lista de colores con "r"
print("Colores con la letra 'r':", colores_con_r)
#%% Explicación del código anterior (colores)
"""
1. Lista original: La lista 'colores' contiene los nombres de los colores que queremos analizar.
2. Nueva lista: Creamos una lista vacía 'colores_con_r' para almacenar los colores que contienen la letra 'r'.
3. Bucle 'for': Recorremos cada elemento de la lista 'colores'.
   - Si el color actual contiene la letra 'r', lo añadimos a la lista 'colores_con_r' usando el método '.append()'.
4. Resultado: Mostramos la nueva lista con los colores que cumplen la condición.
"""

#%% Iterar sobre un string
"""
El siguiente programa recorre cada carácter de una cadena y cuenta cuántas veces aparece la letra 'a'.
"""

# Cadena de texto
cadena = "Python es un lenguaje de programación fantástico"

# Contador de la letra "a"
contador_a = 0

# Bucle for para recorrer la cadena
for caracter in cadena:
    if caracter == "a":    # Verificar si el carácter actual es "a"
        contador_a += 1    # Incrementar el contador

# Mostrar el resultado
print("Número de veces que aparece la letra 'a':", contador_a)

#%% Explicación del código del string
"""
1. Cadena de texto: La variable 'cadena' contiene el texto que queremos analizar.
2. Contador: Inicializamos el contador 'contador_a' en 0.
3. Bucle 'for': Recorremos cada carácter de la cadena.
   - Si el carácter actual es igual a "a", incrementamos el contador.
4. Resultado: Mostramos el número total de veces que aparece la letra "a" en la cadena.
"""
#%% 2. Función 'range'
"""
Introducción a la función 'range'

La función 'range' permite generar una secuencia de números enteros.
Se utiliza comúnmente en bucles 'for' para iterar sobre un rango de valores.

Parámetros de 'range':
- range(max): Genera un rango de números desde '0' hasta 'max - 1'.
- range(min, max): Genera un rango de números desde 'min' hasta 'max - 1'.
- range(min, max, step): Genera un rango desde 'min' hasta 'max - 1', avanzando de acuerdo al valor de 'step'.
"""

#%% Usar 'range' con un parámetro
"""
El siguiente programa imprime los números del '1' al '10' utilizando la función 'range'.
"""

# Usar range con un único parámetro
print("Números del 1 al 10:")
for i in range(1, 11):    # range(max) generará números desde 1 hasta 10 (excluyendo 11)
    print(i, end=" ")     # Usamos end=" " para que los números se impriman en una sola línea

#%% Usar 'range' con dos parámetros
"""
El siguiente programa imprime los números del '5' al '15'.
"""

# Usar range con dos parámetros
print("\nNúmeros del 5 al 15:")
for i in range(5, 16):    # range(min, max) generará números desde 5 hasta 15
    print(i, end=" ")
    #%% Usar 'range' con tres parámetros
"""
El siguiente programa imprime los números del '1' al '10', avanzando de 2 en 2.
"""

# Usar range con tres parámetros
print("\nNúmeros del 1 al 10 con paso 2:")
for i in range(1, 11, 2):    # range(min, max, step) avanzará 2 en 2
   print(i, end=" ")

#%% Usar 'range' con decrementos
"""
El siguiente programa imprime los números del '20' al '0', en pasos de '-2'.
"""

# Usar range con decrementos
print("\nNúmeros del 20 al 0 con paso -2:")
for i in range(20, -1, -2):    # Decrementar desde 20 hasta 0 en pasos de -2
   print(i, end=" ")

#%% Caso especial con 'range'
"""
El siguiente programa intenta generar un rango desde '50' hasta '-1', con un paso positivo de '5'.
Sin embargo, como el inicio es mayor que el final y los pasos son crecientes, la condición nunca se cumple.
"""

# Caso especial con range
print("\nIntentando generar números desde 50 hasta -1 con paso 5:")
for i in range(50, -1, 5):    # Esto no generará ningún número
   print(i, end=" ")

# Resultado esperado: No se imprime nada
print("\nNo se genera ningún número porque el rango no es válido.")
#%% Resumen de la función 'range'
"""
'range' es una herramienta poderosa para generar secuencias de números en Python.

Es importante tener en cuenta la relación entre los parámetros 'min', 'max' y 'step' para garantizar que el rango sea válido:
- Si 'min' < 'max' y 'step' > 0, el rango es creciente.
- Si 'min' > 'max' y 'step' < 0, el rango es decreciente.
- En otros casos, el rango no se genera y el bucle no se ejecuta.
"""

#%% 3. Función 'break' y 'continue'
"""
Modificando la iteración del bucle 'for' con 'break' y 'continue'

En Python, las funciones 'break' y 'continue' permiten modificar el flujo de un bucle 'for' o 'while':

- 'break': Finaliza y sale del bucle inmediatamente cuando se cumple una condición.
- 'continue': Salta al siguiente paso de la iteración, ignorando las sentencias restantes en el bloque del bucle.

Uso de 'break':
Se utiliza para detener el bucle antes de completar todas las iteraciones previstas.

Uso de 'continue':
Se utiliza para omitir ciertas iteraciones sin interrumpir el bucle por completo.

A continuación, exploraremos ejemplos prácticos.
"""

#%% Uso de 'break' para encontrar la posición de un número
"""
El siguiente programa busca el número '9' en una lista y muestra su posición.
Si no se encuentra el número, se imprime un mensaje indicándolo.
"""
#%% Ejemplo con número presente en la lista
# Lista de números
numeros = [1, 3, 5, 9, 11, 13, 15]
# Contador para la posición
posicion = -1  # Iniciamos en -1 para manejar el caso de que no se encuentre el número

for i, num in enumerate(numeros):  # Utilizamos enumerate para obtener índice y valor
    if num == 9:
        posicion = i
        break  # Salimos del bucle cuando encontramos el número

if posicion != -1:
    print(f"El número 9 se encuentra en la posición: {posicion}")
else:
    print("El número 9 no se encuentra en la lista.")

#%% Uso de 'break' con una lista sin el número buscado
"""
¿Qué sucede si el número '9' no está en la lista?
A continuación, vemos cómo se maneja esta situación con el uso de 'for' y 'else'.
"""

# Lista de números sin el número 9
numeros = [2, 4, 6, 8, 10, 12]
posicion = -1

for i, num in enumerate(numeros):
    if num == 9:
        posicion = i
        break
else:  # Este bloque se ejecuta si no se cumple la condición en todo el bucle
    print("El número 9 no se encuentra en la lista.")

if posicion != -1:
    print(f"El número 9 se encuentra en la posición: {posicion}")
    #%% Uso de 'continue' para imprimir solo los números pares
"""
El siguiente programa recorre una lista de números e imprime únicamente los números pares.
Cuando se encuentra un número impar, se omite con el uso de 'continue'.
"""

# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Números pares en la lista:")
for num in numeros:
    if num % 2 != 0:  # Si el número es impar
        continue  # Saltamos al siguiente paso de la iteración
    print(num, end=" ")

#%% Resumen de 'break' y 'continue'
"""
'break':
- Útil para finalizar un bucle antes de recorrer todos los elementos.
- Puede ser combinado con 'if' para cumplir una condición específica.

'continue':
- Permite omitir ciertas iteraciones, avanzando al siguiente paso del bucle.
- Es útil para ignorar elementos no deseados en una secuencia.

Ejemplo práctico:
En una lista de números:
- 'break': Busca un número específico y detiene el bucle al encontrarlo.
- 'continue': Imprime solo los números pares, saltando los impares.

Ejemplos:
1. Hacer un programa mostrar por pantalla los números pares del 0 al 10:
"""

for num in range(0, 11, 2):
    print(num)
    #%% 2. Programa para ingresar nombres a una lista utilizando funciones
# Inicializamos la lista vacía
nombres = []

# Función para ingresar nombres
def ingreso(ele):
    for i in range(0, ele):
        m = input(f"Ingresar Nombre de la posición {i}: ")
        nombres.append(m)

# Preguntamos cuántos elementos tendrá la lista
l = int(input("¿Cuántos elementos tendrá la lista de nombres? "))
ingreso(l)

print("\nLa lista completa de nombres es:\n", nombres)

#%% 3. Imprimir la posición del número 9 en una lista utilizando enumerate
# Lista de números
lista = [2, 4, 5, 7, 8, 19, 3, 4]

# Buscar el número 9
for i, m in enumerate(lista):
    if m == 9:
        break
else:
    # Usamos 'for' junto con 'else' si no se encuentra el número
    i = -1
    print('No se encontró el número 9')

if i >= 0:
    print(i)
#%% 4. Mostrar el orden de los libros de Mario Vargas Llosa
# Lista de libros de Mario Vargas Llosa
obras_mvll = ["La ciudad y los perros", "La casa verde", "Pantaleón y las visitadoras"]

# Lista de orden
orden = ["primer", "segundo", "tercer"]

# Usamos 'enumerate' para recorrer ambas listas
for i, libro in enumerate(obras_mvll):
    print(f"El {orden[i]} libro de Mario Vargas Llosa es: {libro}")

#%% 4. Programa de invitaciones
# Lista de invitados y generación de invitaciones
for name in ["Joel", "Nati", "Jehu", "Angeles", "Maryori", "Lucila", "Mirella", "Cesar"]:
    invitacion = f"Hola {name}, ¡Por favor, ven a mi fiesta el sábado!"
    print(invitacion)
    #%% 5. Programa que suma elementos de una lista sin sum()
def my_sum(xs):
    """Suma los números de una lista `xs`."""
    total = 0
    for x in xs:
        total += x
    return total

# Pruebas
print(my_sum([1, 2, 3, 4]))  # 10
print(my_sum([1.25, 2.5, 1.75]))  # 5.5
print(my_sum([1, -2, 3]))  # 2
print(my_sum(range(11)))  # 55
print(my_sum([]))  # 0

#%% 6. Programa que suma elementos con sum()
m = [1, 2, 3, 4]
print(sum(m))  # Salida: 10

#%% 7. Programa de múltiplos hasta 10
# Función para mostrar los primeros 10 múltiplos de un número
def multiplos(n):
    for i in range(1, 11):
        print(n * i, end=" ")
    print()  # Salto de línea al terminar

# Solicitar número al usuario
m = int(input("Ingrese un número: "))
print(f"\nLos múltiplos de {m} son:")
multiplos(m)
#%% 8. Ejemplo de for anidado (tablas)
# Bucle for anidado con tres niveles
for i in range(4):
    for j in range(4):
        for k in range(2):
            print(i, j, k)

#%% 9. Programa para hallar raíces enésimas
# Solicitar número al usuario
numero = float(input("Ingrese un número: "))
for n in range(2, 101):
    raiz = numero ** (1 / n)
    print(f"La raíz {n}-ésima de {numero} es {raiz}")

