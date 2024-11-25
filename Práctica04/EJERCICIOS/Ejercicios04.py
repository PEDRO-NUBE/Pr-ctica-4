# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:12:38 2024

@author: HP
"""

#%% Ejercicios 1, 2 y 3
{
  "metadata": {
    "kernelspec": {
      "name": "python",
      "display_name": "Python (Pyodide)",
      "language": "python"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "python",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.8"
    }
  },
  "nbformat_minor": 4,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "code",
      "source": "x = int(input(\"ingrese numero inicial: \"))\ny = int(input(\"ingrese numero final: \"))\n#z = int(input(\"ingrese numero intervalo de numero: \"))\nk = list(range(x-1,y+1))\nfor i in k:\n    #if i % 2 !=0:\n    if i % 2 ==0:\n        print(i)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": "x = int(input(\"ingrese numero inicial: \"))\ny = int(input(\"ingrese numero final: \"))\n#z = int(input(\"ingrese numero intervalo de numero: \"))\nfor i in range(x-1,y+1):\n    print(i)",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    },
    {
      "cell_type": "code",
      "source": "\n\n",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}
#%% Programa 4: Hacer un programa que verifique los comentarios de los alumnos EPIT
# Función para verificar si un comentario es positivo o negativo
def verificar_comentario(comentario):
    # Listas de palabras negativas y positivas
    palabras_negativas = ["malo", "pesimo", "no", "horrible", "terrible"]
    palabras_positivas = ["bueno", "excelente", "bien", "fantastico", "maravilloso"]
    
    # Convertir el comentario a minúsculas para evitar problemas de mayúsculas/minúsculas
    comentario = comentario.lower()
    
    # Verificar si contiene palabras negativas
    for palabra in palabras_negativas:
        if palabra in comentario:
            return "Comentario NEGATIVO"
    
    # Verificar si contiene palabras positivas
    for palabra in palabras_positivas:
        if palabra in comentario:
            return "Comentario POSITIVO"
    
    # Si no contiene palabras positivas ni negativas
    return "Comentario NEUTRO"

# Solicitar comentario al usuario
comentario = input("Ingrese el comentario del alumno EPIT: ")

# Verificar el comentario y mostrar el resultado
resultado = verificar_comentario(comentario)
print(resultado)
#%% Programa 5: Generar una lista aleatoria y clasificar en sublistas
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

#%% Programa 6: Verificar números capicúa en un rango
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

#%% Programa 7: Verificar un DNI válido
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
