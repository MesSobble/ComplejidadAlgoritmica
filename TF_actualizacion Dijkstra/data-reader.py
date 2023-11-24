import csv
import numpy

def lector():
    with open('datasetprueba2.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        count = 0
        estaciones = {}
        buses = {}
        est_keys = []
        bus_keys = []
        
        def alreadyExists(arr, n, i = 0):
            if i >= len(arr):
                return -1
            if arr[i] != n:
                return alreadyExists(arr, n, i + 1)
            return i
        
        for row in csv_reader:
            if count > 0:
                label_est = row["Estacion"]
                label_bus = row["Buses"]
                if alreadyExists(est_keys, label_est) == -1:
                    estaciones[label_est] = []
                    est_keys.append(label_est)
                
                if alreadyExists(bus_keys, label_bus) == -1:
                    buses[label_bus] = []
                    bus_keys.append(label_bus)
                
                estaciones[label_est].append((row["Buses"], row["Tarifa"]))
                buses[label_bus].append((row["Estacion"], row["Tarifa"]))
            
            count += 1
        
        #return estaciones, buses
        print(estaciones["Benavides"])
lector()