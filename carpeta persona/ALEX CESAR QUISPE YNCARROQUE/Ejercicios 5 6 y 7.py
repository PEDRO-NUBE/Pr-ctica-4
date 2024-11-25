# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:12:38 2024

@author: HP
"""

#%% Programa 1: Generar una lista aleatoria y clasificar en sublistas
### Descripción:
# Hacer un programa que genere una lista aleatoria de hasta 60 números.
# Luego, subdividirla en listas de múltiplos de 2, 3 y 5.

import random

# Función para generar una lista aleatoria de hasta 60 números
def generar_lista_aleatoria():
    return [random.randint(1, 100) for _ in range(60)]

# Función para clasificar números en múltiples listas
def clasificar_multiplos(lista):
    multiplos_2 = []
    multiplos_3 = []
    multiplos_5 = []
    
    for num in lista:
        if num % 2 == 0:
            multiplos_2.append(num)
        if num % 3 == 0:
            multiplos_3.append(num)
        if num % 5 == 0:
            multiplos_5.append(num)
    
    return multiplos_2, multiplos_3, multiplos_5

# Generar y clasificar
lista = generar_lista_aleatoria()
multiplos_2, multiplos_3, multiplos_5 = clasificar_multiplos(lista)

print(f"Lista completa: {lista}")
print(f"Múltiplos de 2: {multiplos_2}")
print(f"Múltiplos de 3: {multiplos_3}")
print(f"Múltiplos de 5: {multiplos_5}")

#%% Programa 2: Verificar números capicúa en un rango
### Descripción:
# Solicitar un número inicial de 3 cifras y un número final de 4 cifras.
# Recorrer el rango e imprimir cuáles números son capicúa.

# Función para verificar si un número es capicúa
def es_capicua(numero):
    str_num = str(numero)
    return str_num == str_num[::-1]

# Solicitar los valores inicial y final
inicio = int(input("Ingrese un número inicial de 3 cifras: "))
final = int(input("Ingrese un número final de 4 cifras: "))

# Generar el rango de números
rango = list(range(inicio, final + 1))

# Verificar cuáles son capicúa
print("Números capicúa en el rango:")
for num in rango:
    if es_capicua(num):
        print(num)

#%% Programa 3: Verificar un DNI válido
### Descripción:
# Solicitar un DNI y verificar que:
# - No contenga letras ni símbolos extraños.
# - Tenga exactamente 8 dígitos.

# Función para verificar si un DNI es válido
def verificar_dni(dni):
    if len(dni) != 8:
        return False
    if not dni.isdigit():
        return False
    return True

# Solicitar el DNI al usuario
while True:
    dni = input("Ingrese su DNI (8 dígitos): ")
    if verificar_dni(dni):
        print("DNI válido.") 
        break
    else:
        print("DNI inválido. Por favor, intente de nuevo.")
