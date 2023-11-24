#Generador de información
# Importamos lo necesario para generar las listas
import json
import pandas as pd
import numpy as np
import random
from os.path import exists


#Aquí estarán los diccionarios

#Definimos una función que convierte una matriz a CSV (guardar la información)
def MatrixToCSV(matrix):
  tabla = pd.DataFrame(matrix)
  tabla.to_csv('Estaciones_Buses.csv', index=False)

#Crea los valores aleatoreos
def randomMatrix(nrow: int, ncol: int):
  matrix = np.zeros((nrow, ncol))
  i = 0
  j = 0
  while i < nrow:
    j = 0
    while j < ncol:
      n = random.choice([1.5, 2.5, 0])#random.randint(0,1)
      matrix[i,j] = n
      j = j + 1
    i = i + 1
  #convertimos la matriz a un CSV, para no tener que hacer esto cada vez que iniciamos el programa
  MatrixToCSV(matrix)
  return matrix

#lee el archivo
def readCSV(nrow = 0, ncol = 0):
  if exists('Estaciones_Buses.csv'):
    matrix = np.loadtxt(open("Estaciones_Buses.csv", "rb"), delimiter=",", skiprows=1)
    return matrix
  else:
    return randomMatrix(nrow, ncol)

#obtenemos las estaciones
def getEstaciones( nrow: int, ncol: int):
  matrix = readCSV(nrow, ncol)
  Estaciones = {}
  label = ''
  arr = []
  aux = ""
  i = 0
  j = 0
  #verificamos filas
  while i < nrow:
    j = 0
    label = f'Estación {i + 1}'
    arr = []
    while j < ncol:
      if matrix[i][j] > 0:
        #aux = random.choice([f'Bus {j + 1}', f'Expreso {j + 1}'])
        arr.append((f'Bus {j + 1}', matrix[i][j]))
      #avanzamos en columnas
      j = j + 1
    #avanzamos en filas
    i = i + 1
    Estaciones[label] = arr
  return Estaciones

#obtenemos las estaciones
def getBuses( nrow: int, ncol: int):
  matrix = readCSV(nrow, ncol)
  Buses = {}
  label = ''
  arr = []
  aux = ""
  i = 0
  j = 0
  #verificamos columnas
  while j < ncol:
    i = 0
    #aux = random.choice([f'Bus {j + 1}', f'Expreso {j + 1}'])
    label = f'Bus {j + 1}'
    arr = []
    while i < nrow:
      if matrix[i][j] > 0:
        arr.append(f'Estación {i + 1}')
      i = i + 1
    j = j + 1
    Buses[label] = arr
  return Buses
