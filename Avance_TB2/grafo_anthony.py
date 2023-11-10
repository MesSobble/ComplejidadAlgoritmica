import random_anthony as rA

import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import *
from tkinter import Tk, Label, Button, Frame, PhotoImage
from tkinter.ttk import *
from tkinter.font import Font
from tkinter.constants import CENTER, SE


def dibujar_grafo(nodo_inicial = 'Estación 1'):
    estaciones = rA.getEstaciones(25, 5)
    buses = rA.getBuses(25, 5)
    
    # Crear un grafo vacío
    G = nx.Graph()
    
    # Agregar nodos y aristas al grafo según los datos en los diccionarios
    for estacion, conexiones in estaciones.items():
        G.add_node(estacion)
        for conexion in conexiones:
            G.add_weighted_edges_from([(estacion, conexion[0], conexion[1])])
    
    for bus, rutas in buses.items():
        for ruta in rutas:
            G.add_weighted_edges_from([(bus, ruta[0], ruta[1])])
    
    # Elegir un nodo inicial para BFS
    
    bfs_tree = nx.Graph(nx.bfs_edges(G, source=nodo_inicial))
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(bfs_tree, seed=42)  # Posición de los nodos
    nx.draw(bfs_tree, pos, with_labels=True, node_size=50, font_size=6, font_color='black')
    plt.title(f'Subgrafo BFS desde {nodo_inicial}')
    plt.show()
    
    #Transforma el grafo en una imagen
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(bfs_tree, seed=42)  # Posición de los nodos
    nx.draw(bfs_tree, pos, with_labels=True, node_size=50, font_size=6, font_color='black')
    plt.title(f'Subgrafo BFS desde {nodo_inicial}')
    plt.axis('off')  # Desactivar ejes

    # Guardar la imagen en un archivo temporal (en el directorio actual)
    img_filename = f"pictures/grafos/grafo_{nodo_inicial}_temp.png"
    plt.savefig(img_filename, format="png")
    plt.close()

    # Cargar la imagen desde el archivo temporal
    img = Image.open(img_filename)
    img = ImageTk.PhotoImage(img)

    # Devolver la imagen
    return img
            

#dibujar_grafo('Estación 1')
#dibujar_grafo('Estación 3')
#dibujar_grafo('Estación 12')