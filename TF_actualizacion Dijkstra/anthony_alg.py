import random_anthony as rA
import matplotlib.pyplot as plt
import queue


Estaciones = rA.getEstaciones(1500, 20)
Buses = rA.getBuses(1500, 20)
#Estaciones = rA.getEstaciones(100, 20)
#Buses = rA.getBuses(100, 20)

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen][destino] = peso
            self.vertices[destino][origen] = peso

    def mostrar_vertices(self):
        return self.vertices
    
    def Dijkstra(self, origen, destino):
        visitados = set()
        cola = queue.PriorityQueue()
        camino = {}
        distancias = {v: float('inf') for v in self.vertices}

        cola.put((0, origen))
        distancias[origen] = 0
        camino[origen] = None

        while not cola.empty():
            peso, nodo_actual = cola.get()

            if nodo_actual == destino:
                break

            if nodo_actual in visitados:
                continue

            visitados.add(nodo_actual)

            for vecino, peso_arista in self.vertices[nodo_actual].items():
                distancia_nueva = distancias[nodo_actual] + peso_arista

                if distancia_nueva < distancias[vecino]:
                    cola.put((distancia_nueva, vecino))
                    distancias[vecino] = distancia_nueva
                    camino[vecino] = nodo_actual

        if destino not in camino:
            return None, float('inf')

        camino_reconstruido = []
        nodo_actual = destino
        while nodo_actual is not None:
            camino_reconstruido.append(nodo_actual)
            nodo_actual = camino[nodo_actual]

        camino_reconstruido.reverse()

        camino_pesos = []
        precio_total = 0
        for p in camino_reconstruido:
            if camino_reconstruido[0] != p:
                precio_total += distancias[p]
            camino_pesos.append((p, distancias[p]))

        return camino_pesos, precio_total
        
    
    def BFS(self, origen, destino):
        visitados = set()
        cola = queue.Queue()
        camino = {}

        cola.put(origen)
        visitados.add(origen)
        camino[origen] = None

        while not cola.empty():
            nodo_actual = cola.get()

            if nodo_actual == destino:
                break

            for vecino in self.vertices[nodo_actual]:
                if vecino not in visitados:
                    cola.put(vecino)
                    visitados.add(vecino)
                    camino[vecino] = nodo_actual

        if destino not in camino:
            return None, float('inf')


        camino_reconstruido = []
        nodo_actual = destino
        while nodo_actual is not None:
            camino_reconstruido.append(nodo_actual)
            nodo_actual = camino[nodo_actual]

        camino_reconstruido.reverse()
        distancia_total = len(camino_reconstruido) - 1
        return camino_reconstruido, distancia_total
    
    
mi_grafo = Grafo()


for nodo in Buses.keys():
    mi_grafo.agregar_vertice(nodo)

for nodo in Estaciones.keys():
    mi_grafo.agregar_vertice(nodo)

for origen, destinos in Estaciones.items():
    for destino in destinos:
        mi_grafo.agregar_arista(origen, destino[0], destino[1])

for origen, destinos in Buses.items():
    for destino in destinos:
        mi_grafo.agregar_arista(origen, destino[0], destino[1])

#print("grafo")
#print(mi_grafo.mostrar_vertices())
#print("camino corto")
#print(mi_grafo.BFS("Estación 3", "Estación 5"))
#print("camino barato")
#print(mi_grafo.PRIM("Estación 3", "Estación 5"))

#bus = Estaciones['Estación 1'][1][0]
#precio = Estaciones['Estación 1'][1][1]
#print(f'{bus} a precio de {precio}')