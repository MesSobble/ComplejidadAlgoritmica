import csv
import random

# Especifica el nombre del archivo CSV
nombre_archivo = "datasetprueba2.csv"

# Define los encabezados de las columnas
encabezados = ["ID", "Buses", "Estacion","Rutas","Tarifa", "Altitud", "Longitud"]

# Crea una lista para almacenar los datos
datos = []

# Genera datos al azar y agréga a la lista
for i in range(1, 1501):  # Crea 1500 filas de datos
    id = i
    
    Buses = ["Expreso1", "Expreso2", "Expreso3", "Expreso4", "Expreso5", "Expreso6", "Expreso7", "Expreso8", "Expreso9","SX", "SXN", "A", "B", "C", "D"]
    
    Estaciones = ["Estacion A", "Estacion B", "Estacion C", "Estacion D", "Estacion E", "Estacion F", "Naranjal","Izaguirre", "Pacifico", "Independencia", "Los jasmines", "Tomas Valle", "El milagro", "Honorio Delgado", "Uni", "Parque del trabajo", "Caqueta", "Dos de Mayo", 
                "Quilca", "España", "Ramon", "Tacna", "Jiron de la Union", "Colmena", "Central", "Estadio Nacional", "Mexico", "Canada", "Javier Prado",
                "Canaval Moreyra", "Aramburu", "Domingo Orue", "Angamos", "Ricardo Palma", "Benavides", "28 de Julio", "Plaza de Flores", "Balta", "Bulevar", "Estadio Union","Escuela Militar",
                "Teran", "Rosario de Villa", "Matellini"]
    
    
    bus = random.choice(Buses) # bus al azar
    
    estacion = random.choice(Estaciones)  # estacion al azar
    
    tarifa = random.choice([1.5, 2.5])
    if tarifa == 2.5:
        ruta = "Ruta Troncal"
    else:
        ruta = "Alimentador"
    
    
    altitud = random.randint(-10000, -5000)
    
    latitud = random.randint(-80000, -70000)
    
    datos.append([id, bus, estacion, ruta, tarifa, altitud, latitud])

# Escribe los datos en el archivo CSV
with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)

    escritor_csv.writerow(encabezados)  # Escribe la fila de encabezados

    for fila in datos:
        escritor_csv.writerow(fila)  # Escribe cada fila de datos

print(f"Se ha creado el archivo {nombre_archivo} con datos al azar.")