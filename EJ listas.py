# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 09:11:34 2025

@author: B09S115est
"""

#Ejercicio con listas y funciones




#aqui generamos la lista
import random 

def visualizar_lista(la_lista):
    for posicion in range(0, len(la_lista)):
        if (posicion + 1) % 10 == 0:
            print()
        else:
            print(la_lista[posicion],'\t', end="")
            
def obtener_lista_pares(la_lista):
    lista_numeros_pares = []
    for i in range(0,len(la_lista)):
        if la_lista[i] % 2 ==0:
            lista_numeros_pares.append(la_lista[i])
    return lista_numeros_pares

def obtener_lista_impares(la_lista):
    lista_numeros_pares = []
    for i in range(0,len(la_lista)):
        if la_lista[i] % 2 !=0:
            lista_numeros_pares.append(la_lista[i])
    return lista_numeros_pares
        
#aqui esta la funcion principal
print('Programa para generar una lista de 100 numeros enteros aleatorios')
    
la_lista = []
for i in range (0,100):
    numero = random.randint(0, 99)
    la_lista.append(numero)
    
print('la lista generada es:')
visualizar_lista(la_lista)
    
    
lista_pares = obtener_lista_impares(la_lista)
print('la lista con numeros pares es:')
obtener_lista_pares(la_lista)

lista_impares = obtener_lista_impares(la_lista)
print('la lista con numeros impares es: ')
obtener_lista_impares()

 