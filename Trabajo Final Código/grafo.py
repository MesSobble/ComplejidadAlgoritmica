import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
from tkinter import *
from tkinter import Tk, Label, Button, Frame, PhotoImage
from tkinter.ttk import *
from tkinter.font import Font
from tkinter.constants import CENTER, SE


def dibujar_grafo():
    estaciones = {
        'Estacion A': ['Estacion B', 'Estacion C'],
        'Estacion B': ['Estacion A', 'Estacion D'],
        'Estacion C': ['Estacion A', 'Estacion E'],
        'Estacion D': ['Estacion B', 'Estacion F'],
        'Estacion E': ['Estacion C'],
        'Estacion F': ['Estacion D'],
        'Naranjal': ['Expreso2', 'Expreso3', 'Expreso4', 'Expreso5', 'SX', 'SXN', 'A', 'B', 'D'],
        'Izaguirre': ['A', 'B', 'D', 'Expreso4', 'Expreso6', 'Expreso8'],
        'Pacifico': ['A', 'B', 'D'],
        'Independencia': ['A', 'B', 'D', 'Expreso5', 'Expreso6', 'Expreso8'],
        'Los Jasmines': ['A', 'B', 'D'],
        'Tomas Valle': ['A', 'B', 'D', 'Expreso4', 'Expreso5', 'Expreso7', 'Expreso8'],
        'El Milagro': ['A', 'B', 'D'],
        'Honorio Delgado': ['A', 'B', 'D'],
        'Uni': ['A', 'B', 'D', 'Expreso2', 'Expreso4', 'Expreso5', 'Expreso8', 'Expreso9'],
        'Parque del Trabajo': ['A', 'B', 'D'],
        'Caqueta': ['A', 'B', 'D', 'Expreso4', 'Expreso5', 'Expreso8', 'Expreso9'],
        'Dos de Mayo': ['B', 'D', 'Expreso4'],
        'Quilca': ['A', 'B', 'D'],
        'España': ['A', 'B', 'D', 'Expreso4', 'Expreso5', 'Expreso8'],
        'Ramon Castilla':['A', 'C'],
        'Tacna':['A', 'C'],
        'Jiron de la Union':['A', 'C'],
        'Colmena':['A', 'C'],
        'Central': ['A', 'B', 'C', 'D', 'Expreso1', 'Expreso4', 'Expreso5', 'Expreso6', 'Expreso7', 'Expreso8', 'SXN'],
        'Estadio Nacional': ['B', 'C', 'Expreso1'],
        'Mexico': ['B', 'C'],
        'Canada': ['B', 'C', 'Expreso2', 'Expreso5', 'Expreso9'],
        'Javier Prado': ['B', 'C', 'Expreso1', 'Expreso2', 'Expreso4', 'Expreso5', 'Expreso6', 'Expreso7', 'Expreso8'],
        'Canaval Moreyra': ['B', 'C', 'Expreso1', 'Expreso4', 'Expreso5', 'Expreso6', 'Expreso7', 'Expreso8', 'Expreso8', 'SX'],
        'Aramburu': ['B', 'C', 'SX'],
        'Domingo Orue': ['B', 'C'],
        'Angamos': ['B', 'C', 'Expreso1', 'Expreso3', 'Expreso4', 'Expreso5', 'Expreso6', 'Expreso7', 'Expreso8', 'Expreso9'],
        'Ricardo Palma': ['B', 'C', 'Expreso5'],
        'Benavides': ['B', 'C', 'Expreso3', 'Expreso6', 'Expreso8', 'Expreso9'],
        '28 de Julio': ['B', 'C', 'Expreso1'],
        'Plaza de Flores': ['B', 'C', 'Expreso4', 'Expreso5', 'Expreso8'],
        'Balta': ['B', 'C', 'Expreso1'],
        'Bulevar': ['B', 'C', 'Expreso1'],
        'Estadio Union': ['B', 'C', 'Expreso1'],
        'Escuela Militar': ['B', 'C', 'Expreso1'],
        'Teran': ['B', 'C', 'Expreso1'],
        'Rosario de Villa': ['B', 'C', 'Expreso1'],
        'Matellini': ['B', 'C', 'Expreso1']
    }

    buses= {
        'Expreso1': ['Central', 'Estadio Nacional', 'Javier Prado', 'Canaval Moreyra', 'Angamos', '28 de Julio', 'Balta', 'Bulevar', 'Estadio Union', 'Escuela Militar', 'Teran', 'Rosario de Villa', 'Matellini'],
        'Expreso2': ['Naranjal', 'Canada', 'Javier Prado', 'Ricardo Palma', '28 de Julio'],
        'Expreso3': ['Naranjal', 'Angamos', 'Benavides'],
        'Expreso4': ['Naranjal', 'Izaguirre', 'Tomas Valle', 'Uni', 'Caqueta', 'Dos de Mayo', 'España', 'Central', 'Javier Prado', 'Canaval Moreyra', 'Angamos', 'Plaza de Flores'],
        'Expreso5': ['Naranjal', 'Independencia', 'Tomas Valle', 'Uni', 'España', 'Central', 'Canada', 'Javier Prado', 'Canaval Moreyra', 'Angamos', 'Ricardo Palma', 'Plaza de Flores'],
        'Expreso6': ['Izaguirre', 'Independencia', 'Central', 'Javier Prado', 'Canaval Moreyra', 'Angamos', 'Benavides'],
        'Expreso7': ['Tomas Valle', 'Central', 'Javier Prado', 'Canaval Moreyra', 'Angamos'],
        'Expreso8': ['Izaguirre', 'Independencia', 'Tomas valle', 'Uni', 'Caqueta', 'España', 'Central', 'Javier Prado', 'Canaval Moreyra', 'Angamos', 'Benavides', 'Plaza de Flores'],
        'Expreso9': ['Uni', 'Caqueta', 'Canada', 'Canaval Moreyra', 'Angamos', 'Benavides'],
        'SX': ['Naranjal', 'Canaval Moreyra', 'Aramburu'],
        'SXN':['Naranjal', 'Central'],
        'A':['Naranjal', 'Izaguirre', 'Pacifico', 'Independencia','Los Jasmines', 'Tomas Valle', 'El Milagro', 'Honorio Delgado', 'Uni', 'Parque del Trabajo', 'Caqueta', 'Ramon Castilla', 'Tacna', 'Jiron de la Union', 'Colmena', 'Central'],
        'B':['Naranjal', 'Izaguirre', 'Pacifico', 'Independencia','Los Jasmines', 'Tomas Valle', 'El Milagro', 'Honorio Delgado', 'Uni', 'Parque del Trabajo', 'Caqueta', 'Dos de Mayo', 'Quilca', 'España', 'Central', 'Estadio Nacional',
            'Mexico', 'Canada', 'Javier prado', 'Canaval Moreyra', 'Aramburu', 'Domingo Orue', 'Angamos', 'Ricardo Palma', 'Benavides','28 de Julio', 'Plaza de Flores', 'Balta', 'Bulevar', 'Estadio Union', 'Escuela Militar', 'Teran', 'Rosario de Villa', 'Matellini' ],
        'C':['Ramon Castilla', 'Tacna', 'Jiron de la Union', 'Colmena', 'Central', 'Estadio Nacional', 'Javier Prado', 'Canaval Moreyra', 'Angamos', '28 de Julio', 'Balta', 'Bulevar', 'Estadio Union', 'Escuela Militar', 'Teran', 'Rosario de Villa', 'Matellini'],
        'D':['Naranjal', 'Izaguirre', 'Pacifico', 'Independencia','Los Jasmines', 'Tomas Valle', 'El Milagro', 'Honorio Delgado', 'Uni', 'Parque del Trabajo', 'Caqueta', 'Dos de Mayo', 'Quilca', 'España', 'Central']
    }
    

    # Crear un grafo vacío
    G = nx.Graph()

    # Agregar nodos y aristas al grafo según los datos en los diccionarios
    for estacion, conexiones in estaciones.items():
        G.add_node(estacion)
        for conexion in conexiones:
            G.add_edge(estacion, conexion)

    for bus, rutas in buses.items():
        for ruta in rutas:
            G.add_edge(bus, ruta)

    # Elegir un nodo inicial para BFS
    nodo_inicial = 'Naranjal'

    # Realizar BFS desde el nodo inicial
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
    img_filename = "pictures/grafos/grafo_temp.png"
    plt.savefig(img_filename, format="png")
    plt.close()

    # Cargar la imagen desde el archivo temporal
    img = Image.open(img_filename)
    img = ImageTk.PhotoImage(img)

    # Devolver la imagen
    return img

dibujar_grafo()